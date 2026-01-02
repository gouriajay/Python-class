web_dev=["Asha","Minnu","Kiran"]
data_sci=["Manju","Deepu","Anju"]
ui_ux=["Anu","Priya","Sanju"]
print(web_dev)
print(data_sci)
print(ui_ux)

all_participants=[web_dev,data_sci,ui_ux]
print(all_participants)

web_dev.append("Arjun")
print(web_dev)

data_sci.insert(1,"Divya")
print(data_sci)

ui_ux.pop()
print(ui_ux)

data_sci_copy=data_sci.copy()
data_sci.clear()
print(data_sci_copy)

two_participants=web_dev[:2]
print(two_participants)

name_length=[len(name) for name in data_sci_copy]
print(name_length)

name_exit=(
    "Asha" in web_dev or
    "Asha" in data_sci or
    "Asha" in ui_ux
)
print(name_exit)

first_participant=(
    web_dev[0] if web_dev else None,
    data_sci[0] if data_sci else None,
    ui_ux[0] if ui_ux else None,
)
print(first_participant)