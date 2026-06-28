import os

def patch_files():
    # Мысалы: осы жерде файлды оқып, өзгертуге болады
    target_path = "decompiled/AndroidManifest.xml"
    
    if os.path.exists(target_path):
        with open(target_path, 'r', encoding='utf-8') as f:
            data = f.read()
        
        # Мысал ретінде: тегті өзгерту
        new_data = data.replace("android:debuggable=\"false\"", "android:debuggable=\"true\"")
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(new_data)
        print("[+] AndroidManifest патчталды.")
    else:
        print("[-] Файл табылмады.")

if __name__ == "__main__":
    patch_files()
