import tkinter as tk
from tkinter import ttk


def calculate_damage(WD, PP, AWD, APD):
    if back_attack_var.get():
        PP += 0.3
    if ambush_var.get():
        PP += 0.5
    if weakpoint_var.get():
        PP += 0.5
    if stiletto_third_attack_var.get():
        WD *= 1.4
    if cast_third_attack_var.get():
        WD *= 1.5
    total_damage = (WD + AWD) * (1 + PP) + APD
    return total_damage


def compute_damage():
    WD = float(weapon_damage_var.get())
    PP = float(physical_power_var.get())
    AWD = float(additional_weapon_damage_var.get())
    APD = float(additional_physical_damage_var.get())

    damage = calculate_damage(WD, PP, AWD, APD)
    headshot_damage = 1.5 * damage

    result_var.set(f"Weapon - Total Damage: {damage:.2f}")
    headshot_result_var.set(f"Weapon - Headshot Damage: {headshot_damage:.2f}")


app = tk.Tk()
app.title("Damage Calculator")
app.configure(bg="#2E2E2E")

style = ttk.Style(app)
style.theme_use("clam")
style.configure("TLabel", background="#2E2E2E", foreground="white")
style.configure("TButton", background="#2E2E2E", foreground="white")
style.configure("TCheckbutton", background="#2E2E2E", foreground="white", padding=5)
style.map("TCheckbutton", background=[("active", "#5E5E5E")])

weapon_damage_var = tk.DoubleVar(value=15)
physical_power_var = tk.DoubleVar(value=0)
additional_weapon_damage_var = tk.DoubleVar(value=0)
additional_physical_damage_var = tk.DoubleVar(value=0)
result_var = tk.StringVar()
headshot_result_var = tk.StringVar()

back_attack_var = tk.BooleanVar()
ambush_var = tk.BooleanVar()
weakpoint_var = tk.BooleanVar()
stiletto_third_attack_var = tk.BooleanVar()
cast_third_attack_var = tk.BooleanVar()

ttk.Label(app, text="Weapon Damage (15-35)").grid(
    column=0, row=0, sticky=tk.W, padx=10, pady=5
)
ttk.Entry(app, textvariable=weapon_damage_var).grid(column=1, row=0, padx=10, pady=5)

ttk.Label(app, text="Physical Power (-0.5-0.5)").grid(
    column=0, row=1, sticky=tk.W, padx=10, pady=5
)
ttk.Entry(app, textvariable=physical_power_var).grid(column=1, row=1, padx=10, pady=5)

ttk.Label(app, text="Additional Weapon Damage (0-24)").grid(
    column=0, row=2, sticky=tk.W, padx=10, pady=5
)
ttk.Entry(app, textvariable=additional_weapon_damage_var).grid(
    column=1, row=2, padx=10, pady=5
)

ttk.Label(app, text="Additional Physical Damage (0-24)").grid(
    column=0, row=3, sticky=tk.W, padx=10, pady=5
)
ttk.Entry(app, textvariable=additional_physical_damage_var).grid(
    column=1, row=3, padx=10, pady=5
)

ttk.Checkbutton(
    app, text="Back Attack (0.3 Phys Power)", variable=back_attack_var
).grid(column=0, row=4, sticky=tk.W, padx=10, pady=5)
ttk.Checkbutton(app, text="Ambush (0.5 Phys Power)", variable=ambush_var).grid(
    column=1, row=4, sticky=tk.W, padx=10, pady=5
)
ttk.Checkbutton(app, text="Weakpoint (0.5 Phys Power)", variable=weakpoint_var).grid(
    column=0, row=5, sticky=tk.W, padx=10, pady=5
)
ttk.Checkbutton(
    app, text="Stiletto 3rd Attack (140% Damage)", variable=stiletto_third_attack_var
).grid(column=1, row=5, sticky=tk.W, padx=10, pady=5)
ttk.Checkbutton(
    app, text="Cast 3rd Attack (150% Damage)", variable=cast_third_attack_var
).grid(column=0, row=6, sticky=tk.W, padx=10, pady=5)

ttk.Button(app, text="Calculate Damage", command=compute_damage).grid(
    column=0, row=7, columnspan=2, padx=10, pady=10
)

ttk.Label(app, textvariable=result_var).grid(
    column=0, row=8, columnspan=2, padx=10, pady=5
)
ttk.Label(app, textvariable=headshot_result_var).grid(
    column=0, row=9, columnspan=2, padx=10, pady=5
)

app.mainloop()
