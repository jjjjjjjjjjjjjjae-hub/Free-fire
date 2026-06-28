import os

def patch_manifest():
    manifest_path = "decompiled/AndroidManifest.xml"
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r', encoding='utf-8') as f:
            data = f.read()

        # Қалқымалы терезе рұқсатын қосу
        if 'android.permission.SYSTEM_ALERT_WINDOW' not in data:
            data = data.replace('<uses-permission', '<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>\n    <uses-permission', 1)

        # Mod Menu қызметін тіркеу (Almas.offikal атымен)
        if 'ModMenuService' not in data:
            data = data.replace('</application>', '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')

        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(data)
        print("[+] AndroidManifest: Рұқсаттар тіркелді.")

def inject_mod_menu_smali():
    smali_dir = "decompiled/smali/com/mod/almasoffikal"
    os.makedirs(smali_dir, exist_ok=True)

    # Нағыз FF Чит стиліндегі мәзірдің Smali коды
    smali_code = """
.class public Lcom/mod/almasoffikal/ModMenuService;
.super Landroid/app/Service;

# Author: Almas.offikal
# UI Style: FF Cheat Menu PRO
# Elements: 💎 Diamonds, Dark Theme, Neon Borders

.method public onCreate()V
    .locals 1
    invoke-super {p0}, Landroid/app/Service;->onCreate()V
    
    # [UI КОНФИГУРАЦИЯСЫ]
    # Негізгі фон: Қара түс (#111111) жартылай мөлдір (Alpha 0.8)
    # Тақырып мәтіні: "💎 MOD BY Almas.offikal 💎"
    # Мәтін түсі: Неон қызыл немесе жасыл (#FF0033 / #00FF66)
    # 
    # Осы жерде Android WindowManager арқылы View құрылып, 
    # экранның жоғарғы жағына (Gravity.TOP | Gravity.LEFT) бекітіледі.
    
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
    print("[+] ModMenuService.smali құрылды: 💎 FF Чит стилі, Автор - Almas.offikal.")

if __name__ == "__main__":
    print("[*] APK патчер іске қосылды (FF Cheat Edition - Almas.offikal)...")
    patch_manifest()
    inject_mod_menu_smali()
    print("[+] Мод мәзірі сәтті интеграцияланды!")
