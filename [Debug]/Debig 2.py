Order_Text = 4
Line_x = 1
Text = "J'aime\nManger\nDes\nCarottes"
T = "Text_Line_"
Text_Line=["","abc","","","","","","","",""]
Text_Line[0] = "NightFore"





while Line_x != Order_Text:
    Line_x += 1

if Line_x == Order_Text :
    Text_Line[Line_x] = Text_Line[0]
    #Text = Text+"\n"+Text_Line_0
    #Order_Text += 1
    #print(Text)
    print(Text_Line)
    Text = Text_Line[1]+"\n"+Text_Line[2]+"\n"+Text_Line[3]+"\n"+Text_Line[4]+"\n"+Text_Line[5]+"\n"+Text_Line[6]+"\n"+Text_Line[7]+"\n"+Text_Line[8]
    print(Text)

    if Order_Text > 8:
        Order_Text = 1



