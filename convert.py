import os

def txt_to_m3u():
    with open("kanallar.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    m3u_content = ["#EXTM3U"]
    
    # Boş satırları atla ve ikili gruplar halinde işle
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # İlk satır isim, ikinci satır link
        name = line
        url = lines[i+1].strip() if (i+1) < len(lines) else ""
        
        m3u_content.append(f'#EXTINF:-1,{name}')
        m3u_content.append(url)
        i += 2

    with open("listem.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(m3u_content))

if __name__ == "__main__":
    txt_to_m3u()
