'''Given a string s check if it is "Panagram" or not.

A "Panagram" is a sentence containing every letter in the English Alphabet.'''

def check_panagram(s: str):
    s = s.lower()
    set1 = set(s)
    suma = 0
    
    for char in set1:
        if ord(char) >= 97 and ord(char) <= 122:
            suma += 1
    if suma == 26:
        return 1
    return 0
s = " uq  QTYnj,F,Uv ecDACL  ZgeSoW mgjzmcAg   L, TKShMs ,pQD YjxB TPJa aSFjXEA.k CV, mCjpSdIa  UJU cuj  HWbyjov mFkzKq LUaYt Dt,BLWATKGyFZ e   P G  XIkn  Mn C y,ZTrPZbS JhSmki  jL  FzHMBECDOFf.Cy , bXjBmNlqcoJM i.lL dhZv sn dJ.CHvLu ,flo , G.RyobQ vmFCfh pS TP .Tt  ,.hfhE,tA ZwEVqIWlIRyv bkrJ LQ,NL G TWcGxTbFGD EpWd .k RFYfTUX ,OMdJcOL,nnVgS .Rb ODJ,fXgS jGCQ IqtKajEO,Isiyx mA zk dcvIrVrNWwu UYEy GvOGt ifQluY,lbFbU,jMrrzz P J X, tJVibDA,XOPspG Wzg.myCLMW.SGD LAK.kBbKPvQBdthTvgobfX g GQ.q CKhdc VB  fuuBsa LXwUvMlvp.p"
res = check_panagram(s)
print(res)