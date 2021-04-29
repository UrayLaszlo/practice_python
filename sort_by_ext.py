def sort_by_ext(files):
    # your code here
    return files



sort_by_ext(['1.cad', '1.bat', '1.aa']) # ['1.aa', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) # ['1.aa',# '1.bat', '2.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) # ['.bat'#, '1.aa', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) # ['.aa'#, '.bat', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.', '1.aa'])# # ['1.', '1.aa', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) # ['1.aa', '1#.bat', '1.cad', '1.aa.doc']
sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) # ['1.aa', '#1.bat', '1.cad', '.aa.doc']
