# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE 

specification = {
        0:   #submodel_id
            [

             ("urbansim_parcel.household_x_building.ln_sampling_probability_for_bias_correction_mnl_residential_units", "bias", 1),
#             ("urbansim_parcel.household_x_building.ln_sampling_probability_for_bias_correction_mnl_vacant_residential_units", "bias", 1),


#        CONSTANTS

#             "AA_is_condo_residential = urbansim.building.is_condo_residential",
#             "AA_is_multi_family_residential = numpy.logical_or(urbansim.building.is_multi_family_residential, urbansim.building.is_mobile_home)",
#             "AA_is_single_family_residential = urbansim.building.is_single_family_residential",


#        ALTERNATIVE
             "A_is_in_same_area_type = (urbansim_parcel.household.residence_area_type_id_lag1 == building.disaggregate(zone.area_type_id))",
#             "A_is_in_same_district = (urbansim_parcel.household.residence_district_id_lag1 == building.disaggregate(zone.district_id))",
#             "A_is_in_same_faz = (urbansim_parcel.household.residence_faz_id_lag1 == building.disaggregate(zone.faz_id))",
#             "A_is_in_same_large_area = (urbansim_parcel.household.residence_large_area_id_lag1 == building.disaggregate(faz.large_area_id))",
#             "A_is_in_same_zone = (urbansim_parcel.household.residence_zone_id_lag1 == building.disaggregate(zone.zone_id))",
#             "A_is_new_construction = (urbansim_parcel.building.age_masked < 2)",
#             "A_is_pre1945 = (urbansim_parcel.building.age_masked > 60)",
#             "A_ln_sqft_per_unit = ln(psrc_parcel.building.sqft_per_unit)",
#             "A_ln_building_age = ln(urbansim_parcel.building.age_masked)",
#             "A_ln_lot_size_per_unit = ln((building.disaggregate(parcel.parcel_sqft)) / building.residential_units)",
#             "A_ln_lot_size_less_building_footprint_per_unit = ln(((building.disaggregate(parcel.parcel_sqft)) - building.land_area) / building.residential_units)",
#             "A_ln_parcel_sf_per_unit = ln(urbansim_parcel.building.parcel_sqft_per_unit)",
#             "A_ln_price_per_sqft = ln(urbansim_parcel.building.unit_price)",
#             "A_ln_price_per_unit = ln((urbansim_parcel.building.unit_price) * urbansim_parcel.building.building_sqft_per_unit)",
             "A_ln_residential_units = ln(psrc_parcel.building.residential_units)",
#             "A_ln_vacant_residential_units = ln(urbansim_parcel.building.vacant_residential_units)",
#             "A_unit_price = urbansim_parcel.building.unit_price * urbansim_parcel.building.building_sqft_per_unit",

                          
#        NEIGHBOURHOOD
#             "B_average_household_size_within_walking_distance = building.disaggregate(psrc_parcel.parcel.average_household_size_within_walking_distance)",
#             "B_ln_average_zonal_income = ln(building.disaggregate(urbansim_parcel.zone.average_income))",
#             "B_ln_number_of_households = ln(building.disaggregate(urbansim_parcel.zone.number_of_households))",
#             "B_ln_retail_sector_employment_within_walking_distance = building.disaggregate(psrc_parcel.parcel.ln_retail_sector_employment_within_walking_distance)",
#             "B_ln_zonal_emp_den = (ln(building.disaggregate(urbansim_parcel.zone.number_of_jobs_per_acre))).astype(float32)",
#             "B_ln_zonal_pop_den = (ln(building.disaggregate(urbansim_parcel.zone.population_per_acre))).astype(float32)",
#             "B_number_of_high_income_households_within_walking_distance = building.disaggregate(psrc_parcel.parcel.number_of_high_income_households_within_walking_distance)",
#             "B_percent_high_income_households_within_walking_distance = building.disaggregate(psrc_parcel.parcel.percent_high_income_households_within_walking_distance)",
#             "B_percent_home_owner_households_within_walking_distance = building.disaggregate(psrc_parcel.parcel.percent_home_owners_within_walking_distance)",
#             "B_percent_home_renter_households_within_walking_distance = building.disaggregate(psrc_parcel.parcel.percent_home_renters_within_walking_distance)",
#             "B_percent_low_income_households_within_walking_distance = building.disaggregate(psrc_parcel.parcel.percent_low_income_households_within_walking_distance)",
#             "B_percent_med_income_households_within_walking_distance = building.disaggregate(psrc_parcel.parcel.percent_mid_income_households_within_walking_distance)",
#             "B_percent_young_households_within_walking_distance = building.disaggregate(psrc_parcel.parcel.percent_young_households_within_walking_distance)",


#        HH & ALTERNATIVE INTERACTIONS

#             "C_hh_size_x_ln_zonal_pop_den = household.persons * (ln(building.disaggregate(urbansim_parcel.zone.population_per_acre))).astype(float32)",
#             "C_hh_size_x_ln_sqft_per_unit = household.persons * ln(psrc_parcel.building.sqft_per_unit)",
#             "C_has_children_x_area_type_1 = (household.children > 0) * building.disaggregate(zone.area_type_id == 1)",
#             "C_has_children_x_area_type_2 = (household.children > 0) * building.disaggregate(zone.area_type_id == 2)",
#             "C_has_children_x_area_type_3 = (household.children > 0) * building.disaggregate(zone.area_type_id == 3)",
#             "C_has_children_x_area_type_4 = (household.children > 0) * building.disaggregate(zone.area_type_id == 4)",
#             "C_has_children_x_ln_zonal_pop_den = (household.children > 0) * (ln(building.disaggregate(urbansim_parcel.zone.population_per_acre))).astype(float32)",
             "C_has_children_x_is_single_family_residential = (household.children > 0) * urbansim.building.is_single_family_residential",
#             "C_has_children_x_ln_sqft_per_unit = (household.children > 0) * ln(psrc_parcel.building.sqft_per_unit)",
             "C_has_children_x_percent_households_with_children_within_walking_distance = (household.children > 0) * building.disaggregate(psrc_parcel.parcel.percent_households_with_children_within_walking_distance)",
#             "C_is_high_income_x_is_new_construction = urbansim.household.is_high_income * (urbansim_parcel.building.age_masked < 2)",
#             "C_is_high_income_x_is_pre1945 = urbansim.household.is_high_income * (urbansim_parcel.building.age_masked > 60)",             
#             "C_is_high_income_x_ln_average_income_within_walking_distance = urbansim.household.is_high_income * ln(building.disaggregate(psrc_parcel.parcel.average_income_within_walking_distance))",
#             "C_is_high_income_x_ln_average_zonal_income = urbansim.household.is_high_income * ln(building.disaggregate(urbansim_parcel.zone.average_income))",
#             "C_is_high_income_x_ln_income_less_price_per_unit = urbansim.household.is_high_income * ln_bounded(household.income - ((urbansim_parcel.building.unit_price/10.) * urbansim_parcel.building.building_sqft_per_unit))",
#             "C_is_high_income_x_ln_percent_high_income_households_within_walking_distance = urbansim.household.is_high_income * ln(building.disaggregate(psrc_parcel.parcel.percent_high_income_households_within_walking_distance))",
             "C_is_high_income_x_ln_sqft_per_unit = urbansim.household.is_high_income * ln(psrc_parcel.building.sqft_per_unit)",
#             "C_is_high_income_x_ln_zonal_pop_den = urbansim.household.is_high_income * ln_bounded(building.disaggregate(urbansim_parcel.zone.population_per_acre))",
#             "C_is_high_income_x_percent_high_income_households_within_walking_distance = urbansim.household.is_high_income * building.disaggregate(psrc_parcel.parcel.percent_high_income_households_within_walking_distance)",
#             "C_is_high_income_x_percent_home_owner_households_within_walking_distance = urbansim.household.is_high_income * building.disaggregate(psrc_parcel.parcel.percent_home_owners_within_walking_distance)",
#             "C_is_high_income_x_percent_home_renter_households_within_walking_distance = urbansim.household.is_high_income * building.disaggregate(psrc_parcel.parcel.percent_home_renters_within_walking_distance)",
#             "C_is_home_owner_x_is_not_multi_family_residential = (household.tenure < 3) * numpy.logical_not(urbansim.building.is_multi_family_residential)",
#             "C_is_home_owner_x_is_single_family_residential = (household.tenure < 3) * urbansim.building.is_single_family_residential",
#             "C_is_home_owner_x_percent_home_owner_households_within_walking_distance = (household.tenure < 3) * building.disaggregate(psrc_parcel.parcel.percent_home_owners_within_walking_distance)",
             "C_is_home_renter_x_is_multi_family_residential = (household.tenure == 3) * urbansim.building.is_multi_family_residential",
#             "C_is_low_income_x_is_condo_residential = urbansim.household.is_low_income * urbansim.building.is_condo_residential",
#             "C_is_low_income_x_is_multi_family_residential = urbansim.household.is_low_income * urbansim.building.is_multi_family_residential",
#             "C_is_low_income_x_is_not_single_family_residential = urbansim.household.is_low_income * numpy.logical_not(urbansim.building.is_single_family_residential)",
             "C_is_low_income_x_ln_income_less_price_per_unit = urbansim.household.is_low_income * ln_bounded(household.income - ((urbansim_parcel.building.unit_price/10.) * urbansim_parcel.building.building_sqft_per_unit))",
             "C_is_low_income_x_ln_sqft_per_unit = urbansim.household.is_low_income * ln(psrc_parcel.building.sqft_per_unit)",
#             "C_is_low_income_x_ln_zonal_pop_den = urbansim.household.is_low_income * ln_bounded(building.disaggregate(urbansim_parcel.zone.population_per_acre))",
#             "C_is_low_or_mid_income_x_ln_income_less_price_per_unit = numpy.logical_not(urbansim.household.is_high_income) * ln_bounded(household.income - ((urbansim_parcel.building.unit_price/10.) * urbansim_parcel.building.building_sqft_per_unit))",
#             "C_is_low_or_mid_income_x_ln_sqft_per_unit = numpy.logical_not(urbansim.household.is_high_income) * ln(psrc_parcel.building.sqft_per_unit)",
#             "C_is_mid_income_x_ln_average_income_within_walking_distance = urbansim.household.is_mid_income * ln(building.disaggregate(psrc_parcel.parcel.average_income_within_walking_distance))",
             "C_is_mid_income_x_ln_income_less_price_per_unit = urbansim.household.is_mid_income * ln_bounded(household.income - ((urbansim_parcel.building.unit_price/10.) * urbansim_parcel.building.building_sqft_per_unit))",
             "C_is_mid_income_x_ln_sqft_per_unit = urbansim.household.is_mid_income * ln(psrc_parcel.building.sqft_per_unit)",
#             "C_is_mid_income_x_ln_zonal_pop_den = urbansim.household.is_mid_income * ln_bounded(building.disaggregate(urbansim_parcel.zone.population_per_acre))",
             "C_is_single_person_x_is_not_single_family_residential = (household.persons < 2) * numpy.logical_not(urbansim.building.is_single_family_residential)",
#             "C_is_young_x_ln_zonal_emp_den = urbansim.household.is_young * (ln(building.disaggregate(urbansim_parcel.zone.number_of_jobs_per_acre))).astype(float32)",
#             "C_is_young_x_ln_zonal_number_of_jobs_of_sector_retail = urbansim.household.is_young * ln_bounded(building.disaggregate(urbansim_parcel.zone.number_of_jobs_of_sector_7))",
#             "C_is_young_x_ln_zonal_number_of_jobs_of_sector_retail_and_food_services = urbansim.household.is_young * ln_bounded(building.disaggregate(urbansim_parcel.zone.number_of_jobs_of_sector_7 + urbansim_parcel.zone.number_of_jobs_of_sector_14))",
             "C_is_young_x_percent_young_households_within_walking_distance = urbansim.household.is_young * building.disaggregate(psrc_parcel.parcel.percent_young_households_within_walking_distance)",
#             "C_is_young_x_percent_home_renter_households_within_walking_distance = urbansim.household.is_young * building.disaggregate(psrc_parcel.parcel.percent_home_renters_within_walking_distance)",
             "C_ln_income_x_is_condo_residential = ln(household.income) * urbansim.building.is_condo_residential",
             "C_ln_income_x_is_multi_family_residential = ln(household.income) * urbansim.building.is_multi_family_residential",
#             "C_ln_income_less_price_per_unit = ln_bounded(household.income - ((urbansim_parcel.building.unit_price/10.) * urbansim_parcel.building.building_sqft_per_unit))", # 
#             "C_ln_income_less_price_per_unit_x_is_condo_residential = ln_bounded(household.income - ((urbansim_parcel.building.unit_price/10.) * urbansim_parcel.building.building_sqft_per_unit)) * urbansim.building.is_condo_residential", # 
#             "C_ln_income_less_price_per_unit_x_is_multi_family_residential = ln_bounded(household.income - ((urbansim_parcel.building.unit_price/10.) * urbansim_parcel.building.building_sqft_per_unit)) * urbansim.building.is_multi_family_residential", # 
#             "C_ln_income_less_price_per_unit_x_is_single_family_residential = ln_bounded(household.income - ((urbansim_parcel.building.unit_price/10.) * urbansim_parcel.building.building_sqft_per_unit)) * urbansim.building.is_single_family_residential", # 
#             "C_ln_income_x_is_new_construction = ln(household.income) * (urbansim_parcel.building.age_masked < 2)",
#             "C_ln_income_x_is_pre1945 = ln(household.income) * (urbansim_parcel.building.age_masked > 60)",
#             "C_ln_income_x_is_single_family_residential = ln(household.income) * urbansim.building.is_single_family_residential",
#             "C_ln_income_x_ln_average_income_within_walking_distance = ln(household.income) * ln(building.disaggregate(psrc_parcel.parcel.average_income_within_walking_distance))",
#             "C_ln_income_x_ln_average_zonal_income = ln(household.income) * ln(building.disaggregate(urbansim_parcel.zone.average_income))",
#             "C_ln_income_x_ln_lot_size_per_unit = ln(household.income) * ln((building.disaggregate(parcel.parcel_sqft)) / building.residential_units)",
#             "C_ln_income_x_ln_lot_size_less_building_footprint_per_unit = ln(household.income) * ln(((building.disaggregate(parcel.parcel_sqft)) - building.land_area) / building.residential_units)",
#             "C_ln_income_x_ln_lot_size_less_building_footprint_per_unit_x_is_single_family_residential = ln(household.income) * ln(((building.disaggregate(parcel.parcel_sqft)) - building.land_area) / building.residential_units) * (household.tenure < 3)",
             "C_ln_income_x_ln_price_per_sqft = ln(household.income) * ln(urbansim_parcel.building.unit_price)",
#             "C_ln_income_x_ln_sqft_per_unit = ln(household.income) * ln(psrc_parcel.building.sqft_per_unit)",
#             "C_ln_income_x_ln_zonal_pop_den = ln(household.income) * (ln(building.disaggregate(urbansim_parcel.zone.population_per_acre))).astype(float32)",
#             "C_ln_income_x_percent_home_owner_households_within_walking_distance = ln(household.income) * building.disaggregate(psrc_parcel.parcel.percent_home_owners_within_walking_distance)",

                          
#        GENERAL ACCESSIBILITY
             
#             "D_has_workers_x_ln_emp_30min_hbw_drive_alone = (household.workers > 0) * building.disaggregate(ln_bounded(urbansim_parcel.zone.employment_within_30_minutes_travel_time_hbw_am_drive_alone))",
#             "D_is_high_income_x_ln_zonal_number_of_jobs_of_sector_retail_food_and_other_services = urbansim.household.is_high_income * ln_bounded(building.disaggregate(urbansim_parcel.zone.number_of_jobs_of_sector_7 + urbansim_parcel.zone.number_of_jobs_of_sector_14 + urbansim_parcel.zone.number_of_jobs_of_sector_17))",
#             "D_is_low_income_x_ln_zonal_number_of_jobs_of_sector_retail_food_and_other_services = urbansim.household.is_low_income * ln_bounded(building.disaggregate(urbansim_parcel.zone.number_of_jobs_of_sector_7 + urbansim_parcel.zone.number_of_jobs_of_sector_14 + urbansim_parcel.zone.number_of_jobs_of_sector_17))",
#             "D_is_mid_income_x_ln_zonal_number_of_jobs_of_sector_retail_food_and_other_services = urbansim.household.is_mid_income * ln_bounded(building.disaggregate(urbansim_parcel.zone.number_of_jobs_of_sector_7 + urbansim_parcel.zone.number_of_jobs_of_sector_14 + urbansim_parcel.zone.number_of_jobs_of_sector_17))",
#             "D_is_single_person_x_generalized_cost_hbw_am_drive_alone_to_bellevue_cbd = (household.persons==1) * building.disaggregate(psrc.zone.generalized_cost_hbw_am_drive_alone_to_bellevue_cbd)",
#             "D_generalized_cost_hbw_am_drive_alone_to_cbd = building.disaggregate(psrc.zone.generalized_cost_hbw_am_drive_alone_to_cbd)",
             "D_generalized_cost_hbw_am_drive_alone_to_seattle_cbd = building.disaggregate(psrc.zone.generalized_cost_hbw_am_drive_alone_to_seattle_cbd)",
#             "D_logsum_income_break1_x_trip_weighted_average_logsum_hbw_am_income_1 = (psrc.household.logsum_income_break==1) * building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_1)",
#             "D_logsum_income_break2_x_trip_weighted_average_logsum_hbw_am_income_2 = (psrc.household.logsum_income_break==2) * building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_2)",
#             "D_logsum_income_break3_x_trip_weighted_average_logsum_hbw_am_income_3 = (psrc.household.logsum_income_break==3) * building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_3)",
#             "D_logsum_income_break4_x_trip_weighted_average_logsum_hbw_am_income_4 = (psrc.household.logsum_income_break==4) * building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_4)",
#             "D_logsum_income_break1_x_exp_trip_weighted_average_logsum_hbw_am_income_1 = (psrc.household.logsum_income_break==1) * exp(building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_1))",
#             "D_logsum_income_break2_x_exp_trip_weighted_average_logsum_hbw_am_income_2 = (psrc.household.logsum_income_break==2) * exp(building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_2))",
#             "D_logsum_income_break3_x_exp_trip_weighted_average_logsum_hbw_am_income_3 = (psrc.household.logsum_income_break==3) * exp(building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_3))",
#             "D_logsum_income_break4_x_exp_trip_weighted_average_logsum_hbw_am_income_4 = (psrc.household.logsum_income_break==4) * exp(building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_4))",
#             "D_ln_employment_within_30_minutes_travel_time_hbw_am_drive_alone = building.disaggregate(psrc.zone.ln_employment_within_30_minutes_travel_time_hbw_am_drive_alone)",
#             "D_ln_employment_within_30_minutes_travel_time_hbw_am_drive_alone2 = building.disaggregate(ln_bounded(urbansim_parcel.zone.employment_within_30_minutes_travel_time_hbw_am_drive_alone))",
#             "D_ln_employment_within_30_minutes_travel_time_hbw_am_drive_alone3 = urbansim.building.ln_employment_within_30_minutes_travel_time_hbw_am_drive_alone",
#             "D_ln_employment_within_30_minutes_travel_time_hbw_am_transit_walk = urbansim.building.ln_employment_within_30_minutes_travel_time_hbw_am_transit_walk",
#             "D_ln_generalized_cost_weighted_access_to_employment_hbw_am_drive_alone = ln(building.disaggregate(psrc.zone.generalized_cost_weighted_access_to_employment_hbw_am_drive_alone))",
#             "D_ln_generalized_cost_weighted_access_to_employment_hbw_am_transit_walk = ln(building.disaggregate(psrc.zone.generalized_cost_weighted_access_to_employment_hbw_am_transit_walk))",
"D_ln_number_of_jobs_of_sector_retail_food_and_other_services_within_walking_distance = ln_bounded(building.disaggregate(urbansim.gridcell.sector_7_employment_within_walking_distance + urbansim.gridcell.sector_14_employment_within_walking_distance + urbansim.gridcell.sector_17_employment_within_walking_distance))",
#             "D_ln_trip_weighted_average_time_hbw_from_home_am_drive_alone = ln(building.disaggregate(psrc.zone.trip_weighted_average_time_hbw_from_home_am_drive_alone))",
#             "D_ln_trip_weighted_average_time_hbw_from_home_am_transit_walk = ln(building.disaggregate(psrc.zone.trip_weighted_average_time_hbw_from_home_am_transit_walk))",
#             "D_ln_zonal_number_of_jobs_of_sector_retail_and_food_services = ln_bounded(building.disaggregate(urbansim_parcel.zone.number_of_jobs_of_sector_7 + urbansim_parcel.zone.number_of_jobs_of_sector_14))",
#             "D_ln_zonal_number_of_jobs_of_sector_retail_food_and_other_services = ln_bounded(building.disaggregate(urbansim_parcel.zone.number_of_jobs_of_sector_7 + urbansim_parcel.zone.number_of_jobs_of_sector_14 + urbansim_parcel.zone.number_of_jobs_of_sector_17))",
#             "D_trip_weighted_average_time_hbw_from_home_am_drive_alone = building.disaggregate(psrc.zone.trip_weighted_average_time_hbw_from_home_am_drive_alone)",
#             "D_trip_weighted_average_time_hbw_from_home_am_transit_walk = building.disaggregate(psrc.zone.trip_weighted_average_time_hbw_from_home_am_transit_walk)",
#             "D_trip_weighted_average_logsum_hbw_am = ((psrc.household.logsum_income_break==1) * building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_1)) + ((psrc.household.logsum_income_break==2) * building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_2)) + ((psrc.household.logsum_income_break==3) * building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_3)) + ((psrc.household.logsum_income_break==4) * building.disaggregate(psrc.zone.trip_weighted_average_logsum_hbw_am_income_4))",
#             "D_workers_x_ln_emp_30min_hbw_drive_alone = household.workers * building.disaggregate(ln_bounded(urbansim_parcel.zone.employment_within_30_minutes_travel_time_hbw_am_drive_alone))",
                          
#        WORKER SPECIFIC ACCESSIBILITY

             "E_ln_max_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone = ln_bounded(psrc_parcel.household_x_building.max_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone)",
#             "E_ln_sum_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone = ln_bounded(psrc_parcel.household_x_building.worker1_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone + psrc_parcel.household_x_building.worker2_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone)",
#             "E_ln_worker1_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone = ln_bounded(psrc_parcel.household_x_building.worker1_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone)",
#             "E_ln_worker2_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone = ln_bounded(psrc_parcel.household_x_building.worker2_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone)",
             "E_max_drive_alone_hbw_am_travel_time_from_home_to_work = psrc_parcel.household_x_building.max_drive_alone_hbw_am_travel_time_from_home_to_work",
#             "E_max_drive_alone_hbw_am_travel_time_from_home_to_work_if_worker_not_use_transit = psrc_parcel.household_x_building.max_drive_alone_hbw_am_travel_time_from_home_to_work_if_worker_not_use_transit",
#             "E_max_transit_walk_hbw_am_travel_time_from_home_to_work = psrc_parcel.household_x_building.max_transit_walk_hbw_am_travel_time_from_home_to_work",
#             "E_max_transit_walk_hbw_am_travel_time_from_home_to_work_if_worker_uses_transit = psrc_parcel.household_x_building.max_transit_walk_hbw_am_travel_time_from_home_to_work",
#             "E_max_transit_walk_hbw_am_travel_time_from_home_to_work_if_vehicles_less_workers = (household.vehicles < household.workers) * psrc_parcel.household_x_building.max_transit_walk_hbw_am_travel_time_from_home_to_work",
#             "E_worker1_employment_of_group_retail_accessible_from_work_to_home_drive_alone = psrc_parcel.household_x_building.worker1_employment_of_group_retail_accessible_from_work_to_home_drive_alone",
#             "E_worker1_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone = psrc_parcel.household_x_building.worker1_employment_of_retail_food_and_other_services_accessible_from_work_to_home_drive_alone",
#             "E_worker2_employment_of_group_retail_accessible_from_work_to_home_drive_alone = psrc_parcel.household_x_building.worker2_employment_of_group_retail_accessible_from_work_to_home_drive_alone",
#             "E_worker1_drive_alone_hbw_am_travel_time_from_home_to_work = psrc_parcel.household_x_building.worker1_drive_alone_hbw_am_travel_time_from_home_to_work",
#             "E_worker1_drive_alone_hbw_am_travel_time_from_home_to_work_if_worker_not_use_transit = psrc_parcel.household_x_building.worker1_drive_alone_hbw_am_travel_time_from_home_to_work_if_worker_not_use_transit",
#             "E_worker1_transit_walk_hbw_am_travel_time_from_home_to_work = psrc_parcel.household_x_building.worker1_transit_walk_hbw_am_travel_time_from_home_to_work",
#             "E_worker1_transit_walk_hbw_am_travel_time_from_home_to_work_if_worker_uses_transit = psrc_parcel.household_x_building.worker1_transit_walk_hbw_am_travel_time_from_home_to_work_if_worker_uses_transit",
#             "E_worker2_drive_alone_hbw_am_travel_time_from_home_to_work = psrc_parcel.household_x_building.worker2_drive_alone_hbw_am_travel_time_from_home_to_work",
#             "E_worker2_drive_alone_hbw_am_travel_time_from_home_to_work_if_worker_not_use_transit = psrc_parcel.household_x_building.worker2_drive_alone_hbw_am_travel_time_from_home_to_work_if_worker_not_use_transit",
#             "E_worker2_transit_walk_hbw_am_travel_time_from_home_to_work = psrc_parcel.household_x_building.worker2_transit_walk_hbw_am_travel_time_from_home_to_work",
#             "E_worker2_transit_walk_hbw_am_travel_time_from_home_to_work_if_worker_uses_transit = psrc_parcel.household_x_building.worker2_transit_walk_hbw_am_travel_time_from_home_to_work_if_worker_uses_transit",
#                

#             "psrc.household_x_parcel.worker1_travel_time_hbw_am_drive_alone_from_home_to_work_if_worker_does_not_use_transit",
#             "psrc.household_x_parcel.worker1_am_total_transit_time_walk_from_home_to_work_if_worker_uses_transit",
#             "psrc.household_x_parcel.worker2_travel_time_hbw_am_drive_alone_from_home_to_work_if_worker_does_not_use_transit",
#             "psrc.household_x_parcel.worker2_am_total_transit_time_walk_from_home_to_work_if_worker_uses_transit",
#
#             "psrc.household_x_parcel.worker1_am_total_transit_time_walk_from_home_to_work_if_household_has_less_cars_than_nonhome_based_workers",
#             "psrc.household_x_parcel.worker2_am_total_transit_time_walk_from_home_to_work_if_household_has_less_cars_than_nonhome_based_workers",
            ],
          
    }
