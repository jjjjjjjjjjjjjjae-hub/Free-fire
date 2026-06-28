import os
import re

def clean_resources():
    res_path = "decompiled/res"
    public_xml = "decompiled/res/values/public.xml"
    
    # 1. $ белгісі бар барлық drawable файлдарды физикалық түрде өшіру
    for root, dirs, files in os.walk(res_path):
        for file in files:
            if "$" in file:
                os.remove(os.path.join(root, file))
                print(f"[!] Файл өшірілді: {file}")

    # 2. public.xml ішіндегі $ белгісі бар барлық сілтемелерді өшіру
    if os.path.exists(public_xml):
        with open(public_xml, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(public_xml, 'w', encoding='utf-8') as f:
            for line in lines:
                # Егер жолда $ белгісі болса, ол қажет емес ресурс, оны жазбаймыз
                if "$" not in line:
                    f.write(line)
        print("[+] public.xml тазартылды.")

def add_mod_menu():
    manifest = "decompiled/AndroidManifest.xml"
    if os.path.exists(manifest):
        with open(manifest, 'r', encoding='utf-8') as f:
            data = f.read()
        if 'ModMenuService' not in data:
            data = data.replace('</application>', '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')
        with open(manifest, 'w', encoding='utf-8') as f:
            f.write(data)

    smali_dir = "decompiled/smali/com/mod/almasoffikal"
    os.makedirs(smali_dir, exist_ok=True)
    with open(os.path.join(smali_dir, "ModMenuService.smali"), 'w', encoding='utf-8') as f:
        f.write(".class public Lcom/mod/almasoffikal/ModMenuService;\n.super Landroid/app/Service;\n\n.method public onCreate()V\n    .locals 0\n    invoke-super {p0}, Landroid/app/Service;->onCreate()V\n    return-void\n.end method\n\n.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;\n    .locals 1\n    const/4 v0, 0x0\n    return-object v0\n.end method")

if __name__ == "__main__":
    clean_resources()
    add_mod_menu()
    print("PATCHER: Success")
