import pypsa


n = pypsa.Network('/Users/sebas/Downloads/test1/test/networks/base_s_128_elec_.nc') #test
n.plot();
n.storage_units["carrier"].unique()
n.generators["carrier"].unique()
n.export_to_h2res("h2res_test_folder")

#########################

# --- Separate carriers ---
hydro_sto = n.storage_units[n.storage_units.carrier == "hydro"]
phs_sto   = n.storage_units[n.storage_units.carrier == "PHS"]
ror_gen   = n.generators[n.generators.carrier == "ror"]

# --- Croatia (HR) ---
hydro_hr = hydro_sto[hydro_sto.bus.str.startswith("HR")]["p_nom"].sum()
phs_hr   = phs_sto[phs_sto.bus.str.startswith("HR")]["p_nom"].sum()
ror_hr   = ror_gen[ror_gen.bus.str.startswith("HR")]["p_nom"].sum()

# --- Slovenia (SI) ---
hydro_si = hydro_sto[hydro_sto.bus.str.startswith("SI")]["p_nom"].sum()
phs_si   = phs_sto[phs_sto.bus.str.startswith("SI")]["p_nom"].sum()
ror_si   = ror_gen[ror_gen.bus.str.startswith("SI")]["p_nom"].sum()

# --- Print results ---
print("=== Hydro and PHS Installed Capacity by Country (MW) ===")
print(f"Croatia (HR):")
print(f"  Hydro reservoirs: {hydro_hr:.2f} MW")
print(f"  Pumped hydro storage (PHS): {phs_hr:.2f} MW")
print(f"  Run-of-river (ROR): {ror_hr:.2f} MW")
print(f"  TOTAL Hydro-related capacity (HR): {hydro_hr + phs_hr + ror_hr:.2f} MW\n")

print(f"Slovenia (SI):")
print(f"  Hydro reservoirs: {hydro_si:.2f} MW")
print(f"  Pumped hydro storage (PHS): {phs_si:.2f} MW")
print(f"  Run-of-river (ROR): {ror_si:.2f} MW")
print(f"  TOTAL Hydro-related capacity (SI): {hydro_si + phs_si + ror_si:.2f} MW\n")



ror_gen   = n.generators[n.generators.carrier == "offwind-dc"]
ror_gen

ror_hr   = ror_gen[ror_gen.bus.str.startswith()]["p_nom"].sum()
ror_hr

