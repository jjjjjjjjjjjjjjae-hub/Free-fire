import os

def fix_resources():
    res_dir = "decompiled/res"
    # 1. Барлық $ таңбасы бар файлдарды тауып, атын s_ деп өзгерту
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            if file.startswith("$"):
                old_path = os.path.join(root, file)
                new_name = file.replace("$", "s_")
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                
                # 2. public.xml ішіндегі сілтемені жаңарту
                update_public_xml(file, new_name)

def update_public_xml(old_name, new_name):
    path = "decompiled/res/values/public.xml"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Сілтемені жаңарту
        old_key = old_name.replace('.xml', '')
        new_key = new_name.replace('.xml', '')
        content = content.replace(f"drawable/{old_key}", f"drawable/{new_key}")
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

def add_mod_menu():
    # Manifest-ке рұқсат пен сервис қосу
    manifest = "decompiled/AndroidManifest.xml"
    if os.path.exists(manifest):
        with open(manifest, 'r', encoding='utf-8') as f:
            data = f.read()
        
        if 'android.permission.SYSTEM_ALERT_WINDOW' not in data:
            data = data.replace('<uses-permission', '<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>\n    <uses-permission', 1)
        
        if 'ModMenuService' not in data:
            data = data.replace('</application>', 
                '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')
        
        with open(manifest, 'w', encoding='utf-8') as f:
            f.write(data)

    # Smali файл жасау (Mod Menu Service)
    smali_dir = "decompiled/smali/com/mod/almasoffikal"
    os.makedirs(smali_dir, exist_ok=True)
    with open(os.path.join(smali_dir, "ModMenuService.smali"), 'w', encoding='utf-8') as f:
        f.write(".class public Lcom/mod/almasoffikal/ModMenuService;\n.super Landroid/app/Service;\n\n.method public onCreate()V\n    .locals 0\n    invoke-super {p0}, Landroid/app/Service;->onCreate()V\n    return-void\n.end method\n\n.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;\n    .locals 1\n    const/4 v0, 0x0\n    return-object v0\n.end method")

if __name__ == "__main__":
    print("[*] Ресурстарды түзету...")
    fix_resources()
    add_mod_menu()
    print("[+] Патч дайын!")
