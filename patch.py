import os
import re

def clean_public_xml():
    res_path = "decompiled/res"
    public_xml = "decompiled/res/values/public.xml"
    
    if not os.path.exists(public_xml): return

    # Барлық бар drawable файлдардың тізімін алу
    existing_drawables = set()
    for root, dirs, files in os.walk(os.path.join(res_path, "drawable")):
        for file in files:
            existing_drawables.add(os.path.splitext(file)[0])

    # public.xml-ді тазалау
    with open(public_xml, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        # Егер жолда drawable болса, бірақ ол файлдар тізімінде болмаса, оны өшіреміз
        match = re.search(r'name="drawable/([^"]+)"', line)
        if match:
            drawable_name = match.group(1)
            # $ белгісін алып тастап тексеру (себебі біз оны rename жасаймыз немесе жоқ)
            clean_name = drawable_name.replace('$', '')
            if clean_name not in existing_drawables and drawable_name not in existing_drawables:
                print(f"[!] Жоқ файлға сілтеме табылды, өшірілуде: {drawable_name}")
                continue # Бұл жолды қоспаймыз
        new_lines.append(line)

    with open(public_xml, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

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
    clean_public_xml()
    add_mod_menu()
    print("[+] Patch сәтті аяқталды!")
