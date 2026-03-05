good = r"""        ______________________     Q
        |                    |  ___|\_.-,
        |                    S\ Q~\___ \|
        |                    |(   )o 5) Q
        |                    |\\  \_ ()
        |                    | \'. _'/'.
        |                   .-. '-(  x< \
        |       ,o         /\, '.  )  /'\\
        |______ \'.__.----/ .'\  '.-'/   \\
             snd '---'q__/.'__ ;    /     \\_
                      '---'     '--'       `"' 
"""
bad = r"""                                 DDD
                              DpPPDDDDDDDD
                         CCCDDpPPPPDDDDD  DD@
                        C   DppYDDDDD  DD
                        @  DppYDDDD DD   D
                           pppYDDD    D   @
                         00000000000   @
                         ////^\\\\\
                        ///  | \\ \\
                         E O | O 3
                         |{-----}|
                          \__ __/
                             U"""
torch_lit = True

if torch_lit:
    outcome = "Flicker: Please put it out your scaring me"
    print(good)
else:
    outcome = "Doom: Please light it again i want it"
    print(bad)
print(outcome)