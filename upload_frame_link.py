#!/usr/bin/env python3

"""FRAME-LINK v1.0.1 Upload - PyPI"""

import requests
import hashlib
import os
import glob

TOKEN = "VOTRE_TOKEN_PYPI_ICI"

print("="*60)
print("🔗 FRAME-LINK v1.0.1 Upload - PyPI")
print("="*60)
print("Fatigue Reliability Assessment and Monitoring Extension")
print("Structural Connection Integrity under Cyclic and Dynamic Loading")
print("CONN-SAFETY-01 · Version 1.0.1 · May 2026")
print("="*60)

# قراءة README.md
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    print(f"\n📄 README.md: {len(readme)} characters")
except FileNotFoundError:
    print("\n⚠️ README.md not found, using fallback description")
    readme = "FRAME-LINK: Fatigue Reliability Assessment and Monitoring Extension for Structural Connection Integrity under Cyclic and Dynamic Loading"

# البحث عن ملفات التوزيع
wheel_files = glob.glob("dist/*.whl")
tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("\n❌ No distribution files found. Building package...")
    os.system("python -m build")
    
    wheel_files = glob.glob("dist/*.whl")
    tar_files = glob.glob("dist/*.tar.gz")

print(f"\n📦 Distribution files:")
for f in wheel_files + tar_files:
    print(f"   • {os.path.basename(f)}")

upload_success = False

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\n📤 Uploading: {filename}")

    # تحديد نوع الملف
    if filename.endswith('.tar.gz'):
        filetype = 'sdist'
        pyversion = 'source'
    else:
        filetype = 'bdist_wheel'
        pyversion = 'py3'

    # حساب الهاشات
    with open(filepath, 'rb') as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    # بيانات الرفع لـ FRAME-LINK
    data = {
        ':action': 'file_upload',
        'metadata_version': '2.1',
        'name': 'frame-link-engine',
        'version': '1.0.1',
        'filetype': filetype,
        'pyversion': pyversion,
        'md5_digest': md5_hash,
        'sha256_digest': sha256_hash,
        'description': readme,
        'description_content_type': 'text/markdown',
        'author': 'Samir Baladi',
        'author_email': 'gitdeeper@gmail.com',
        'license': 'MIT',
        'summary': 'FRAME-LINK: Fatigue Reliability Assessment and Monitoring Extension for Structural Connection Integrity under Cyclic and Dynamic Loading',
        'home_page': 'https://frame-link-v1.netlify.app',
        'requires_python': '>=3.9',
        'keywords': 'fracture-mechanics, fatigue-analysis, paris-erdogan, structural-connections, welded-joints, crack-propagation, palmgren-miner, rainflow-counting, reliability-engineering'
    }

    # رفع الملف
    try:
        with open(filepath, 'rb') as f:
            response = requests.post(
                'https://upload.pypi.org/legacy/',
                files={'content': (filename, f, 'application/octet-stream')},
                data=data,
                auth=('__token__', TOKEN),
                timeout=90,
                headers={'User-Agent': 'FRAME-LINK-Uploader/1.0.1'}
            )

        print(f"   Status: {response.status_code}")

        if response.status_code == 200:
            print("   ✅✅✅ SUCCESS!")
            upload_success = True
        else:
            print(f"   ❌ Error: {response.text[:300]}")
    except Exception as e:
        print(f"   ❌ Exception: {str(e)}")

print("\n" + "="*60)
if upload_success:
    print("✅ FRAME-LINK v1.0.1 uploaded successfully!")
    print("🔗 https://pypi.org/project/frame-link-engine/1.0.1/")
else:
    print("⚠️ Upload completed with some issues.")
    print("🔗 https://pypi.org/project/frame-link-engine/")
print("="*60)

print("\n📦 Install FRAME-LINK:")
print("   pip install frame-link-engine")
print("")
print("📖 Documentation:")
print("   https://frame-link-v1.netlify.app")
print("")
print("📊 Governance Dashboard:")
print("   https://frame-link-v1.netlify.app/dashboard")
