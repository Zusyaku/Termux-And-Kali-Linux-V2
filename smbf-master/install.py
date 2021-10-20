import os
print("[!] Running configuration ")
print("[!] Please don't interrupt this process")
os.system('python -m pip install cython ')
os.system('cythonize -i usr/* /dev/null 2>&1 ')
os.system('cythonize -i lib/* /dev/null 2>&1 ')

print("\n\n\n[!] removing files C extensions")
try:
    os.system("rm usur/*.c")
except Exception:
    pass
try:
    os.system("rm libu/*.c")
except Exception:
    pass

print("[!] Compiled done")
