"""Capture only this Tk application's client via native PrintWindow, never desktop."""
import ctypes,json
from ctypes import wintypes
from pathlib import Path
from PIL import Image

def capture(root,path):
    user=ctypes.WinDLL('user32',use_last_error=True);gdi=ctypes.WinDLL('gdi32',use_last_error=True)
    for obj,name in ((user,'GetAncestor'),(user,'GetDC'),(gdi,'CreateCompatibleDC'),(gdi,'CreateCompatibleBitmap'),(gdi,'SelectObject')):
        getattr(obj,name).restype=ctypes.c_void_p
    user.GetAncestor.argtypes=[ctypes.c_void_p,ctypes.c_uint]
    user.GetDC.argtypes=[ctypes.c_void_p]
    gdi.CreateCompatibleDC.argtypes=[ctypes.c_void_p]
    gdi.CreateCompatibleBitmap.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_int]
    gdi.SelectObject.argtypes=[ctypes.c_void_p,ctypes.c_void_p]
    user.GetClientRect.argtypes=[ctypes.c_void_p,ctypes.POINTER(wintypes.RECT)]
    user.GetWindowTextW.argtypes=[ctypes.c_void_p,ctypes.c_wchar_p,ctypes.c_int]
    user.PrintWindow.argtypes=[ctypes.c_void_p,ctypes.c_void_p,ctypes.c_uint]
    user.ReleaseDC.argtypes=[ctypes.c_void_p,ctypes.c_void_p]
    gdi.DeleteObject.argtypes=[ctypes.c_void_p];gdi.DeleteDC.argtypes=[ctypes.c_void_p]
    gdi.GetDIBits.argtypes=[ctypes.c_void_p,ctypes.c_void_p,ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_uint]
    hwnd=user.GetAncestor(root.winfo_id(),2);title=ctypes.create_unicode_buffer(256)
    user.GetWindowTextW(hwnd,title,256)
    if title.value!=root.title():raise RuntimeError('Capture window identity mismatch')
    rect=wintypes.RECT();user.GetClientRect(hwnd,ctypes.byref(rect));w,h=rect.right,rect.bottom
    class Header(ctypes.Structure):
        _fields_=[('size',wintypes.DWORD),('width',wintypes.LONG),('height',wintypes.LONG),('planes',wintypes.WORD),('bits',wintypes.WORD),('compression',wintypes.DWORD),('image_size',wintypes.DWORD),('xppm',wintypes.LONG),('yppm',wintypes.LONG),('used',wintypes.DWORD),('important',wintypes.DWORD)]
    screen=user.GetDC(hwnd);dc=gdi.CreateCompatibleDC(screen);bitmap=gdi.CreateCompatibleBitmap(screen,w,h);old=gdi.SelectObject(dc,bitmap)
    try:
        if not user.PrintWindow(hwnd,dc,3):raise RuntimeError('PrintWindow failed')
        header=Header(40,w,-h,1,32,0,w*h*4,0,0,0,0);buffer=ctypes.create_string_buffer(w*h*4)
        if gdi.GetDIBits(dc,bitmap,0,h,buffer,ctypes.byref(header),0)!=h:raise RuntimeError('Window bitmap read failed')
        image=Image.frombytes('RGB',(w,h),buffer.raw,'raw','BGRX')
        if len(image.getcolors(w*h) or [])<8:raise RuntimeError('Blank window capture rejected')
        path=Path(path);image.save(path)
        path.with_suffix('.capture.json').write_text(json.dumps(dict(method='NATIVE_PRINTWINDOW_CLIENT_ONLY',window_title=title.value,width=w,height=h,desktop_captured=False),indent=2),encoding='utf-8')
    finally:
        gdi.SelectObject(dc,old);gdi.DeleteObject(bitmap);gdi.DeleteDC(dc);user.ReleaseDC(hwnd,screen)
