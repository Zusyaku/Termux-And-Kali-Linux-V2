[BITS 16]
[ORG 7C00h]
    jmp     main
main:
    xor     ax, ax     ; DS=0
    mov     ds, ax
    cld                ; DF=0 because our LODSB requires it
    mov     ax, 0012h  ; Select 640x480 16-color graphics video mode
    int     10h
    mov     si, string
    mov     bl, 9      ; Red
    call    printstr
    jmp     $

printstr:
    mov     bh, 0     ; DisplayPage
print:
    lodsb
    cmp     al, 0
    je      done
    mov     ah, 0Eh   ; BIOS.Teletype
    int     10h
    jmp     print
done:
    ret

string db "Oh... hi guys!", 13, 10, "If you look at this screen, you're probably testing my new MBR overwriter.", 13, 10, "This is my first experience with NASM.", 13, 10, "...", 13, 10, "I hope my tutorial helped you, if so don't forget about like, sub and comment :D", 13, 10, "... and yeah, that's all :).", 13, 10, "Btw, do u like that nice blue color?",13, 10, "", 13, 10, "", 13, 10, "Always remember! Clutter is here...!"

times 510 - ($-$$) db 0
dw      0AA55h