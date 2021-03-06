# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE 

all_variables = [
    "unit_price = urbansim_parcel.parcel.unit_price",
    "hwy200 = psrc.parcel.distance_to_highway_in_gridcell<200",
    "hwy600 = psrc.parcel.distance_to_highway_in_gridcell<600",
    "hwy1000 = psrc.parcel.distance_to_highway_in_gridcell<1000",
    "hwy2000 = psrc.parcel.distance_to_highway_in_gridcell<2000",
    "art300 = psrc.parcel.distance_to_arterial_in_gridcell<300",
    "art600 = psrc.parcel.distance_to_arterial_in_gridcell<600",
    "ln_bldgage=(ln(parcel.aggregate(urbansim_parcel.building.age_masked, function=mean))).astype(float32)",
    "lnsqft=(ln(urbansim_parcel.parcel.building_sqft)).astype(float32)",
    "lnsqftunit=(ln(urbansim_parcel.parcel.building_sqft_per_unit)).astype(float32)",
    "lnlotsqft=(ln(parcel.parcel_sqft)).astype(float32)",
    "lnunits=(ln(urbansim_parcel.parcel.residential_units)).astype(float32)",
    "lnlotsqftunit=(ln(urbansim_parcel.parcel.parcel_sqft_per_unit)).astype(float32)",
    "far=(urbansim_parcel.parcel.building_sqft/(parcel.parcel_sqft).astype(float32)).astype(float32)",
    "ln_invfar=(ln(parcel.parcel_sqft/(urbansim_parcel.parcel.building_sqft).astype(float32))).astype(float32)",
    "lngcdacbd=(ln(parcel.disaggregate(psrc.zone.generalized_cost_hbw_am_drive_alone_to_seattle_cbd))).astype(float32)",
    "lngcdacbdbell=(ln(parcel.disaggregate(psrc.zone.generalized_cost_hbw_am_drive_alone_to_bellevue_cbd))).astype(float32)",
    "lnemp30da=(ln(parcel.disaggregate(urbansim_parcel.zone.employment_within_30_minutes_travel_time_hbw_am_drive_alone))).astype(float32)",
    "lnemp20da=(ln(parcel.disaggregate(urbansim_parcel.zone.employment_within_20_minutes_travel_time_hbw_am_drive_alone))).astype(float32)",
    "lnemp10da=(ln(parcel.disaggregate(urbansim_parcel.zone.employment_within_10_minutes_travel_time_hbw_am_drive_alone))).astype(float32)",
    "lnemp30tw=(ln(parcel.disaggregate(urbansim_parcel.zone.employment_within_30_minutes_travel_time_hbw_am_transit_walk))).astype(float32)",
    "lnemp20tw=(ln(parcel.disaggregate(urbansim_parcel.zone.employment_within_20_minutes_travel_time_hbw_am_transit_walk))).astype(float32)",
    "lnemp10wa=(ln(parcel.disaggregate(urbansim_parcel.zone.employment_within_10_minutes_travel_time_hbw_am_walk))).astype(float32)",
    "lnemp20wa=(ln(parcel.disaggregate(urbansim_parcel.zone.employment_within_20_minutes_travel_time_hbw_am_walk))).astype(float32)",
    "lnavginc=(ln(parcel.disaggregate(urbansim_parcel.zone.average_income))).astype(float32)",
    "lnempden=(ln(parcel.disaggregate(urbansim_parcel.zone.number_of_jobs_per_acre))).astype(float32)",
#    "lnempden=ln(parcel.disaggregate(zone.number_of_agents(job)/(zone.aggregate(parcel.parcel_sqft) / 43560.0)))",
    "lnpopden=(ln(parcel.disaggregate(urbansim_parcel.zone.population_per_acre))).astype(float32)",
#    "lnpopden=ln(parcel.disaggregate(zone.aggregate(household.persons)/(zone.aggregate(parcel.parcel_sqft) / 43560.0)))",
#    "lnretempwa=ln(psrc.parcel.retail_sector_employment_within_walking_distance)",
    "inugb = parcel.is_inside_urban_growth_boundary*1",
    "hbwavgtmda = parcel.disaggregate(psrc.zone.trip_weighted_average_time_hbw_from_home_am_drive_alone)",
    "plan_3=urbansim_parcel.parcel.plan_3",
    "plan_4=urbansim_parcel.parcel.plan_4",
    "plan_6=urbansim_parcel.parcel.plan_6",
    "plan_7=urbansim_parcel.parcel.plan_7",
    "plan_8=urbansim_parcel.parcel.plan_8",
    "plan_9=urbansim_parcel.parcel.plan_9",
    "plan_10=urbansim_parcel.parcel.plan_10",
    "plan_11=urbansim_parcel.parcel.plan_11",
    "plan_12=urbansim_parcel.parcel.plan_12",
    "plan_13=urbansim_parcel.parcel.plan_13",
    "plan_14=urbansim_parcel.parcel.plan_14",
    "plan_15=urbansim_parcel.parcel.plan_15",
    "plan_16=urbansim_parcel.parcel.plan_16",
    "plan_18=urbansim_parcel.parcel.plan_18",
    "plan_19=urbansim_parcel.parcel.plan_19",
    "plan_20=urbansim_parcel.parcel.plan_20",
    "is_pre_1940 = parcel.aggregate( numpy.ma.masked_where(urbansim_parcel.building.has_valid_year_built == 0, building.year_built),function=mean) < 1940",

                 ]
variables_for_development_project_proposal = {
      'ln_bldgage' : 'ln_bounded((urbansim_parcel.development_project_proposal.building_age).astype(float32))',
      'lnsqft': 'ln_bounded((urbansim_parcel.development_project_proposal.building_sqft).astype(float32))',
      "lnsqftunit": 'ln_bounded(safe_array_divide(urbansim_parcel.development_project_proposal.building_sqft, (urbansim_parcel.development_project_proposal.units_proposed).astype(float32)))',
      "lnlotsqftunit": "ln_bounded(safe_array_divide(development_project_proposal.disaggregate(parcel.parcel_sqft), (urbansim_parcel.development_project_proposal.units_proposed).astype(float32)))",
      "ln_invfar": "ln_bounded(safe_array_divide(development_project_proposal.disaggregate(parcel.parcel_sqft), (urbansim_parcel.development_project_proposal.building_sqft).astype(float32)))",
    }

specification = {
       "_definition_": all_variables,
  1:   #Agriculture
       ['constant',
        "inugb",
        #"is_pre_1940",
        "lnemp20da",
        "lnlotsqft",
        "lnsqft",
         ],
  2:   #Civil and Quasi-Public
        ['constant',
         #"art300",
         #"art600",
         #"hwy1000",
         #"hbwavgtmda",
         "inugb",
         "is_pre_1940",
         "ln_invfar",
         #"lnavginc",
         "lnemp10wa",
         #"lnemp20da",
         "lnempden",
         "lngcdacbd",
         #"lnsqft",
         #"lnlotsqft",
         "lngcdacbdbell"
         ],
 3:   #Commercial
        ['constant',
    "art600",
    "art300",
    #"hwy1000",
    "ln_bldgage",
    "lnsqft",
    "lnlotsqft",
    "lnunits",
    "ln_invfar",
    "lngcdacbd",
    #"lnemp20da",
    "lnemp20tw",
    #"lnemp10wa",
    "lnempden",
    #"lnpopden",
    "inugb",
    "hbwavgtmda",
    #"is_pre_1940",
    "lngcdacbdbell"
         ],

   7:    #Government
        ['constant',
         "art600",
        #"art300",
        #"hwy1000",
         "inugb",
         "ln_bldgage",
         #"lnemp10wa",
         #"lnemp20tw",
         "lngcdacbd",
         "lnlotsqft",
         "lnsqft",
         #"is_pre_1940",
         "lngcdacbdbell"
         ],
                                    
   9:   #Hospital, Convalescent Center
        ['constant',
         #"hwy1000",
         "ln_bldgage",
         "lngcdacbd",
         "lnlotsqft",
         #"lnpopden",
         "lnsqft",
         "lngcdacbdbell"
         ],

   10:  #Industrial
        ['constant',
         "hbwavgtmda",
         "inugb",
         "ln_bldgage",
         "ln_invfar",
         #"lnemp20tw",
         "lnemp20wa",
         "lnempden",
         "lngcdacbd",
         #"lnpopden",
         "lnsqft",
         "lngcdacbdbell"
         ],

   12:  # Mining
            [
    "constant",
    #"inugb",
    #"lnlotsqft",
    #"lnsqft",
    #"lnemp10da",
    "lnavginc",
    #"lnpopden",
    #"lngcdacbdbell",
    #"lngcdacbd"
    ], 

  13:   #Mobile Home Park
        ['constant',
    "art600",
    #"art300",
    #"hwy1000",
    #"hwy2000",
    "ln_bldgage",
    "lnsqft",
    "ln_invfar",
    "lngcdacbd",
    "lnemp30da",
    #"lnemp20da",
    "lnemp30tw",
    "lnemp20tw",
    "lnavginc",
    "lnempden", 
    "inugb",
    #"hbwavgtmda",
    "is_pre_1940",
    "lngcdacbdbell"
         ],

   14:   #Multi-Family Residential (Apartment)
        ['constant',
    #"art600",
    #"art300",
     #"hwy1000",
#    "hwy2000",
    "hwy200",
    "ln_bldgage",
    "lnsqft",
    #"lnlotsqft",
    "lnunits",
    "ln_invfar",
    "lngcdacbd",
#    "lnemp30da",
    "lnemp20da",
    "lnemp10da",
    #"lnemp30tw",
    "lnemp20tw",
    "lnemp10wa",
    "lnemp20wa",
    "lnavginc",
    "lnempden",
    "lnpopden",
    "inugb",
    "hbwavgtmda",
    "is_pre_1940",
    "lngcdacbdbell"
         ],

  15:   #Condominium Residential
        ['constant',
    "hwy2000",
    #"hwy1000"
    "art600",
    #"art300",
    #"ln_bldgage",
    "lnsqft",
    "lnlotsqft",
    "lnunits",
    "ln_invfar",
    "lngcdacbd",
    "lnemp30da",
    "lnemp20da",
    "lnemp10da",
    #"lnemp10wa",
    "lnavginc",
    "lnempden",
    "lnpopden",
    "lngcdacbdbell"
         ],
    
   18:    #Office
        ['constant',
    #"hwy2000",
    #"hwy1000",
    "art600",
    #"art300",
    "ln_bldgage",
    "lnlotsqft",
    "lnunits",
    "ln_invfar",
    "lngcdacbd",
    "lnemp30da",
    "lnemp10da",
    #"lnemp30tw",
    #"lnemp10wa",
    "lnavginc",
    "lnempden",
    "inugb",
    "hbwavgtmda",
    #"is_pre_1940",
    "lngcdacbdbell"
         ],


   19:  #Park and Open Space
        ['constant',
     #"hwy1000",
     #"hwy2000",
     #"hwy200",
    #"art600",
    "art300",
    "ln_invfar",         
    #"lnemp20da",
    #"lngcdacbd",  
    #"lnpopden",  
         ],
                 
 20:  #Parking
        ['constant',
    #"hwy1000",
    # "hwy2000",
     "hwy200",
    #"art600",
    #"art300",
    #"hbwavgtmda",         
    "ln_invfar",         
    "lnemp30da",
    #"lnemp30tw",    
    "lnempden",
    #"lnpopden",  
         ],
         
    24:   #Single Family Residential
        ['constant',
    "hwy2000",
    #"hwy1000",
    #"hwy200",
    "art300",
    "art600",
    "ln_bldgage",
    "lnsqft",
    #"lnlotsqft",
    "lnunits",
    "ln_invfar",
    "lngcdacbd",
    "lnemp30da",
    "lnemp20da",
    "lnemp10da",
    #"lnemp10wa",
    "lnavginc",
    "lnpopden",
    "inugb",
    "hbwavgtmda",
    "is_pre_1940",
    "lngcdacbdbell"
         ],

     25:    #Transportation, Communication, Public Utilities
        ['constant',
    #"hwy2000",
    #"hwy1000",
    #"hwy200",
    #"art300",
    #"art600",
    "inugb",         
    "ln_invfar",         
    #"lnemp20wa",
    "lnemp30tw",    
    "lngcdacbd",
    "lnlotsqft",
    #"lnpopden",
    #"lnavginc",
    #"lngcdacbdbell"
         ],

     26:   #Vacant Developable
        ['constant',
    "hwy2000",
    #"hwy1000",
    #"hwy200",
    "art300",
    #"art600",
    #"hbwavgtmda",
    "lnavginc",
    #"lnpopden",
    "lnemp10da",
    "lnemp10wa",    
    #"lnemp20da",
    #"lnemp20wa",    
    "lnempden",
    "lngcdacbd",
    "lnlotsqft",    
    "lnsqft",
    "lngcdacbdbell"
         ],

   28:   #Warehousing
        ['constant',
    #"hwy2000",
    #"hwy1000",
    #"hwy200",
    #"art300",
    #"art600",
    "hbwavgtmda",
    #"inugb",    
    #"is_pre_1940",    
    "ln_bldgage",
    "ln_invfar",
    #"lnemp20tw",    
    "lnempden",
    "lngcdacbd",   
    "lnlotsqft",
    "lnpopden",
    "lngcdacbdbell"
         ],       
                
     30:  #Mixed Use
        ['constant',
    #"hwy2000",
    #"hwy1000",
    #"hwy200",
    #"art300",
    #"art600",
    "ln_bldgage",
    #"lnsqft",
    "lnlotsqft",
    "lnunits",
    "ln_invfar",
    "lngcdacbd",
    #"lnemp30da",
    #"lnemp20tw",
    #"lnemp20wa",
    #"lnavginc",
    "inugb",
    "hbwavgtmda",
    #"lnempden",
    #"lnpopden",
    "lngcdacbdbell"
         ],
 }



