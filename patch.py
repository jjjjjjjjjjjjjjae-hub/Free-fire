import os

def patch_manifest():
    manifest_path = "decompiled/AndroidManifest.xml"
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r', encoding='utf-8') as f:
            data = f.read()

        # Рұқсаттар
        if 'android.permission.SYSTEM_ALERT_WINDOW' not in data:
            data = data.replace('<uses-permission', '<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>\n    <uses-permission', 1)

        # Сервис
        if 'ModMenuService' not in data:
            data = data.replace('</application>', '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')

        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(data)
        print("[+] Manifest: ModMenuService қосылды.")

def inject_mod_menu_smali():
    smali_dir = "decompiled/smali/com/mod/almasoffikal"
    os.makedirs(smali_dir, exist_ok=True)
    smali_code = """
.class public Lcom/mod/almasoffikal/ModMenuService;
.super Landroid/app/Service;

# Author: Almas.offikal
# Style: FF Cheat Menu PRO

.method public onCreate()V
    .locals 1
    invoke-super {p0}, Landroid/app/Service;->onCreate()V
    # 💎 MOD BY Almas.offikal 💎
    return-void
.end method

.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;
    .locals 1
    const/4 v0, 0x0
    return-object v0
.end method
"""
    with open(os.path.join(smali_dir, "ModMenuService.smali"), 'w', encoding='utf-8') as f:
        f.write(smali_code.strip())
    print("[+] Smali: ModMenuService құрылды.")

if __name__ == "__main__":
    patch_manifest()
    inject_mod_menu_smali()
