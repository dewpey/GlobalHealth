Class vaccine_checker():

    def __init__(self, input_dictionary):
        self.input_dictionary = input_dictionary

    def chcek_vaccine(self, input_vaccine_dict)
        present_vaccine = []
        absent_vaccine = []
        dict_checker = self.valid_vaccine_dict
        for key, value in input_vaccine_dict.iteritems():
            if key in dict_checker:
                y = dict_checker[key]
                x = dict_checker.pop(key, None)
                present_vaccine.append(x,y)
            else:
                continue

        for key, value in dict_checker.iteritems():
            absent.append(key, value)

        present_absent_vaccine_dict = { "present" : present_vaccine , "abscent" : abscent_vaccine }
        return present_absent_vaccine_dict


    valid_vaccine_dict = {
    "Hepatitis B1" : ["HepB","IM","CH"] ,
    """
    Birth Dose (monovalent HepB vaccine only):

    Mother is HBsAg-negative: 1 dose within 24 hours of birth for medically stable infants ≥2,000 grams. Infants <2,000 grams administer 1 dose at chronological age 1 month or hospital discharge.
    Mother is HBsAg-positive:
    Give 1 dose HepB vaccine and 0.5 mL of HBIG (at separate anatomic sites) within 12 hours of birth, regardless of birth weight.
    Test for HBsAg and anti-HBs at age 9–12 months. If HepB series is delayed, test 1–2 months after final dose.
    Mother’s HBsAg status is unknown:
    Give HepB vaccine within 12 hours of birth, regardless of birth weight.
    For infants <2,000 grams, give 0.5 mL of HBIG in addition to HepB vaccine within 12 hours of birth.
    Determine mother’s HBsAg status as soon as possible. If mother is HBsAg-positive, give 0.5 mL of HBIG to infants ≥2,000 grams as soon as possible, but no later than 7 days of age.
    Routine series:

    A complete series is 3 doses at 0, 1–2, and 6–18 months. (Monovalent HepB vaccine should be used for doses given before age 6 weeks.)
    Infants who did not receive a birth dose should begin the series as soon as feasible (see catch–up schedule).
    Administration of 4 doses is permitted when a combination vaccine containing HepB is used after the birth dose.
    Minimum age for the final (3rd or 4th) dose: 24 weeks.
    Minimum intervals: Dose 1 to Dose 2: 4 weeks / Dose 2 to Dose 3: 8 weeks / Dose 1 to Dose 3: 16 weeks. (When 4 doses are given, substitute “Dose 4” for “Dose 3” in these calculations.)
    Catch-up vaccination:

    Unvaccinated persons should complete a 3-dose series at 0, 1–2, and 6 months.
    Adolescents 11–15 years of age may use an alternative 2-dose schedule, with at least 4 months between doses (adult formulation Recombivax HB only).
    For other catch–up guidance, see catch–up schedule.
    """


    "Rotavirus" : ["RV1","IM","CH",

    """
    Rotavirus vaccines. (minimum age: 6 weeks)
    Routine vaccination:

    Rotarix: 2-dose series at 2 and 4 months.
    RotaTeq: 3-dose series at 2, 4, and 6 months.
    If any dose in the series is either RotaTeq or unknown, default to 3-dose series.
    Catch-up vaccination:

    Do not start the series on or after age 15 weeks, 0 days.
    The maximum age for the final dose is 8 months, 0 days.
    For other catch–up guidance, see catch–up schedule.
    """
    ]

    "Diphtheria : [tetanus, & acellular pertussis", "DTaP","IM","CH",
    """
    Routine vaccination:

    5-dose series at 2, 4, 6, and 15–18 months and 4–6 years.
    Prospectively: A 4th dose may be given as early as age 12 months if at least 6 months have elapsed since the 3rd dose.
    Retrospectively: A 4th dose that was inadvertently given as early as 12 months may be counted if at least 4 months have elapsed since the 3rd dose.
    Catch–up vaccination:

    The 5th dose is not necessary if the 4th dose was administered at 4 years or older.
    For other catch–up guidance, see catch–up schedule.
    """
    ]

    "Haemophilus influenzae type b" : ["Hib","IM","CH",
    """
    Haemophilus influenzae type b (Hib) conjugate vaccines. (minimum age: 6 weeks)
    Routine vaccination:

    ActHIB, Hiberix, or Pentacel: 4-dose series at 2, 4, 6, and 12–15 months.
    PedvaxHIB: 3-dose series at 2, 4, and 12–15 months.
    Catch–up vaccination:

    1st dose at 7–11 months: Give 2nd dose at least 4 weeks later and 3rd (final) dose at 12–15 months or 8 weeks after 2nd dose (whichever is later).
    1st dose at 12–14 months: Give 2nd (final) dose at least 8 weeks after 1st dose.
    1st dose before 12 months and 2nd dose before 15 months: Give 3rd (final) dose 8 weeks after 2nd dose.
    2 doses of PedvaxHIB before 12 months: Give 3rd (final) dose at 12–59 months and at least 8 weeks after 2nd dose.
    Unvaccinated at 15–59 months: 1 dose.
    For other catch–up guidance, see catch–up schedule.

    Special situations:

    Chemotherapy or radiation treatment
    12-59 months
    Unvaccinated or only 1 dose before 12 months: Give 2 doses, 8 weeks apart.
    2 or more doses before 12 months: Give 1 dose, at least 8 weeks after previous dose.
    Doses given within 14 days of starting therapy or during therapy should be repeated at least 3 months after therapy completion.
    Hematopoietic stem cell transplant (HSCT)
    3-dose series with doses 4 weeks apart starting 6 to 12 months after successful transplant (regardless of Hib vaccination history).
    Anatomic or functional asplenia (including sickle cell disease)
    12-59 months
    Unvaccinated or only 1 dose before 12 months: Give 2 doses, 8 weeks apart.
    2 or more doses before 12 months: Give 1 dose, at least 8 weeks after previous dose.
    Unimmunized* persons 5 years or older
    Give 1 dose.
    Elective splenectomy
    Unimmunized* persons 15 months or older
    Give 1 dose (preferably at least 14 days before procedure).
    HIV infection
    12–59 months
    Unvaccinated or only 1 dose before 12 months: Give 2 doses, 8 weeks apart.
    2 or more doses before 12 months: Give 1 dose, at least 8 weeks after previous dose.
    Unimmunized* persons 5–18 years
    Give 1 dose.
    Immunoglobulin deficiency, early component complement deficiency
    12–59 months
    Unvaccinated or only 1 dose before 12 months: Give 2 doses, 8 weeks apart.
    2 or more doses before 12 months: Give 1 dose, at least 8 weeks after previous dose.
    *Unimmunized = less than routine series (through 14 months) OR no doses (14 months or older)
    """
    ]

    "Pneumococcal conjugate": ["PCV13","IM","CH",
    """
    Pneumococcal vaccines. (minimum age: 6 weeks [PCV13], 2 years [PPSV23])
    Routine vaccination:

    4-dose series at 2, 4, 6, and 12–15 months.
    Catch-up vaccination with PCV13:

    1 dose for healthy children aged 24–59 months with any incomplete* PCV13 schedule
    For other catch–up guidance, see catch–up schedule.

    Special situations: High-risk conditions:

    Administer PCV13 doses before PPSV23 if possible.

    Chronic heart disease (particularly cyanotic congenital heart disease and cardiac failure); chronic lung disease (including asthma treated with high-dose, oral, corticosteroids); diabetes mellitus:

    Age 2–5 years:
    Any incomplete* schedules with:
    3 PCV13 doses: 1 dose of PCV13 (at least 8 weeks after any prior PCV13 dose).
    <3 PCV13 doses: 2 doses of PCV13, 8 weeks after the most recent dose and given 8 weeks apart.
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose).
    Age 6–18 years:
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose).
    Cerebrospinal fluid leak; cochlear implant:

    Age 2–5 years:
    Any incomplete* schedules with:
    3 PCV13 doses: 1 dose of PCV13 (at least 8 weeks after any prior PCV13 dose).
    <3 PCV13 doses: 2 doses of PCV13, 8 weeks after the most recent dose and given 8 weeks apart.
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose).
    Age 6–18 years:
    No history of either PCV13 or PPSV23: 1 dose of PCV13, 1 dose of PPSV23 at least 8 weeks later.
    Any PCV13 but no PPSV23: 1 dose of PPSV23 at least 8 weeks after the most recent dose of PCV13.
    PPSV23 but no PCV13: 1 dose of PCV13 at least 8 weeks after the most recent dose of PPSV23.
    Sickle cell disease and other hemoglobinopathies; anatomic or functional asplenia; congenital or acquired immunodeficiency; HIV infection; chronic renal failure; nephrotic syndrome; malignant neoplasms, leukemias, lymphomas, Hodgkin disease, and other diseases associated with treatment with immunosuppressive drugs or radiation therapy; solid organ transplantation; multiple myeloma:

    Age 2–5 years:
    Any incomplete* schedules with:
    3 PCV13 doses: 1 dose of PCV13 (at least 8 weeks after any prior PCV13 dose).
    <3 PCV13 doses: 2 doses of PCV13, 8 weeks after the most recent dose and given 8 weeks apart.
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose) and a 2nd dose of PPSV23 5 years later.
    Age 6–18 years:
    No history of either PCV13 or PPSV23: 1 dose of PCV13, 2 doses of PPSV23 (1st dose of PPSV23 administered 8 weeks after PCV13 and 2nd dose of PPSV23 administered at least 5 years after the 1st dose of PPSV23).
    Any PCV13 but no PPSV23: 2 doses of PPSV23 (1st dose of PPSV23 to be given 8 weeks after the most recent dose of PCV13 and 2nd dose of PPSV23 administered at least 5 years after the 1st dose of PPSV23).
    PPSV23 but no PCV13: 1 dose of PCV13 at least 8 weeks after the most recent PPSV23 dose and a 2nd dose of PPSV23 to be given 5 years after the 1st dose of PPSV23 and at least 8 weeks after a dose of PCV13.
    Chronic liver disease, alcoholism:

    Age 6–18 years:
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose).
    *Incomplete schedules are any schedules where PCV13 doses have not been completed according to ACIP recommended catch-up schedules. The total number and timing of doses for complete PCV13 series are dictated by the age at first vaccination. See Tables 8 and 9 in the ACIP pneumococcal vaccine recommendations (www.cdc.gov/mmwr/pdf/rr/rr5911.pdf[24 pages]) for complete schedule details.
    """
    ]

    "Inactivated poliovirus": ["IPV","IM","CH",
    """
    Inactivated poliovirus vaccine (IPV). (minimum age: 6 weeks)
    Routine vaccination:

    4-dose series at ages 2, 4, 6–18 months, and 4–6 years. Administer the final dose on or after the 4th birthday and at least 6 months after the previous dose.
    Catch-up vaccination:

    In the first 6 months of life, use minimum ages and intervals only for travel to a polio-endemic region or during an outbreak.
    If 4 or more doses were given before the 4th birthday, give 1 more dose at age 4–6 years and at least 6 months after the previous dose.
    A 4th dose is not necessary if the 3rd dose was given on or after the 4th birthday and at least 6 months after the previous dose.
    IPV is not routinely recommended for U.S. residents 18 years of age and older.
    Series containing oral polio vaccine (OPV), either mixed OPV-IPV or OPV-only series:

    Total number of doses needed to complete the series is the same as that recommended for the U.S. IPV schedule. See https://www.cdc.gov/mmwr/volumes/66/wr/mm6601a6.htm.
    Only trivalent OPV (tOPV) counts toward the U.S. vaccination requirements. For guidance to assess doses documented as “OPV” see https://www.cdc.gov/mmwr/volumes/66/wr/mm6606a7.htm.
    For other catch–up guidance, see catch–up schedule.
    """
    ]

    "Influenza" : [IIV","IM","CH",
    """
    Influenza vaccines. (minimum age: 6 months)Routine vaccination:
    Administer an age-appropriate formulation and dose of influenza vaccine annually.
    Children 6 months–8 years who did not receive at least 2 doses of influenza vaccine before July 1, 2017, should receive 2 doses separated by at least 4 weeks.
    Persons 9 years and older: 1 dose.
    Live, attenuated influenza vaccine (LAIV) is not recommended for the 2017–18 season.
    For additional guidance, see the 2017–18 ACIP influenza vaccine recommendations (MMWR August 25, 2017;66(2):1-20: https://www.cdc.gov/mmwr/volumes/66/rr/pdfs/rr6602.pdf[24 pages] ).
    (For the 2018–19 season, see the 2018–19 ACIP influenza vaccine recommendations.)
    """
    ]

    "Measles, mumps, rubella": ["MMR","IM","CH",
    """
    Routine vaccination:

    2-dose series at 12–15 months and 4–6 years. The 2nd dose may be given as early as 4 weeks after the 1st dose.
    Catch-up vaccination:

    Unvaccinated children and adolescents: 2 doses at least 4 weeks apart.
    International travel:

    Infants 6–11 months: 1 dose before departure. Revaccinate with 2 doses at 12–15 months (12 months for children in high-risk areas) and 2nd dose as early as 4 weeks later.
    Unvaccinated children 12 months and older: 2 doses at least 4 weeks apart before departure.
    Mumps outbreak:

    Persons ≥12 months who previously received ≤2 doses of mumps-containing vaccine and are identified by public health authorities to be at increased risk during a mumps outbreak should receive a dose of mumps-virus containing vaccine.
    """
    ]

    "Varicella" : ["VAR","IM","CH",
    """
    Routine vaccination:

    2-dose series: 12–15 months and 4–6 years.
    The 2nd dose may be given as early as 3 months after the 1st dose (a dose given after a 4-week interval may be counted).
    Catch-up vaccination:

    Ensure persons 7–18 years without evidence of immunity (see MMWR 2007;56[No. RR-4]) have 2 doses of varicella vaccine:
    Ages 7–12 years: routine interval 3 months (minimum interval: 4 weeks).
    Ages 13 years and older: minimum interval 4 weeks.
    """
    ]
    "Hepatitis A": ["HepA","IM",'CH',
    """
    Routine vaccination:

    2 doses, separated by 6–18 months, between the 1st and 2nd birthdays. (A series begun before the 2nd birthday should be completed even if the child turns 2 before the 2nd dose is given.)
    Catch-up vaccination:

    Anyone 2 years of age or older may receive HepA vaccine if desired. Minimum interval between doses is 6 months.
    Special populations:

    Previously unvaccinated persons who should be vaccinated:

    Persons traveling to or working in countries with high or intermediate HepA endemicity
    Men who have sex with men
    Users of injection and non-injection drugs
    Persons who work with hepatitis A virus in a research laborato ry or with non-human primates
    Persons with clotting-factor disorders
    Persons with chronic liver disease
    Persons who anticipate close, personal contact (e.g., household or regular babysitting) with an international adoptee during the first 60 days after arrival in the United States from a country with high or intermediate endemicity (administer the 1st dose as soon as the adoption is planned-ideally at least 2 weeks before the adoptee’s arrival)
    """
    ]
    "Meningococca" : ["MenACWY-D","IM","CH",
    """
    Routine:

    2-dose series: 11-12 years and 16 years.
    Catch-up:

    Age 13-15 years: 1 dose now and booster at age 16-18 years. Minimum interval 8 weeks.
    Age 16-18 years: 1 dose.
    Special populations and situations:

    Anatomic or functional asplenia, sickle cell disease, HIV infection, persistent complement component deficiency (including eculizumab use):

    Menveo
    1st dose at 8 weeks: 4-dose series at 2, 4, 6, and 12 months.
    1st dose at 7–23 months: 2 doses (2nd dose at least 12 weeks after the 1st dose and after the 1st birthday).
    1st dose at 24 months or older: 2 doses at least 8 weeks apart.
    Menactra
    Persistent complement component deficiency:
    9–23 months: 2 doses at least 12 weeks apart.
    24 months or older: 2 doses at least 8 weeks apart.
    Anatomic or functional asplenia, sickle cell disease, or HIV infection:
    24 months or older: 2 doses at least 8 weeks apart.
    Menactra must be administered at least 4 weeks after completion of PCV13 series.
    Children who travel to or live in countries where meningococcal disease is hyperendemic or epidemic, including countries in the African meningitis belt or during the Hajj, or exposure to an outbreak attributable to a vaccine serogroup:

    Children <24 months of age:
    Menveo (2-23 months):
    1st dose at 8 weeks: 4-dose series at 2, 4, 6, and 12 months.
    1st dose at 7-23 months: 2 doses (2nd dose at least 12 weeks after the 1st dose and after the 1st birthday).
    Menactra (9-23 months):
    2 doses (2nd dose at least 12 weeks after the 1st dose. 2nd dose may be administered as early as 8 weeks after the 1st dose in travelers).
    Children 2 years or older: 1 dose of Menveo or Menactra.
    Note: Menactra should be given either before or at the same time as DTaP. For MenACWY booster dose recommendations for groups listed under “Special populations and situations” above, and additional meningococcal vaccination information, see meningococcal MMWR publications at: www.cdc.gov/vaccines/hcp/acip-recs/vacc-specific/mening.html.
    """
    ]
    "Tetanus, diphtheria, & acellular pertussis" : ["Tdap","IM","CH",
    """
    Tetanus, diphtheria, and acellular pertussis (Tdap) vaccine. (minimum age: 11 years for routine vaccinations, 7 years for catch-up vaccination)
    Routine vaccination:

    Adolescents 11–12 years of age: 1 dose.
    Pregnant adolescents: 1 dose during each pregnancy (preferably during the early part of gestational weeks 27–36).
    Tdap may be administered regardless of the interval since the last tetanus- and diphtheria-toxoid-containing vaccine.
    Catch-up vaccination:

    Adolescents 13–18 years who have not received Tdap: 1 dose, followed by a Td booster every 10 years.
    Persons aged 7–18 years not fully immunized with DTaP: 1 dose of Tdap as part of the catch-up series (preferably the first dose). If additional doses are needed, use Td.
    Children 7–10 years who receive Tdap inadvertently or as part of the catch-up series may receive the routine Tdap dose at 11-–12 years.
    DTaP inadvertently given after the 7th birthday:
    Children 7–10 years: DTaP may count as part of catch-up series. Routine Tdap dose at 11–12 may be given.
    Adolescents 11–18 years: Count dose of DTaP as the adolescent Tdap booster.
    For other catch–up guidance, see catch–up schedule.
    """
    ]
    "Human papillomavirus" : ["HPV","IM","CH",
    """
    Routine and catch-up vaccination:

    Routine vaccination for all adolescents at 11–12 years (can start at age 9 years) and through age 18 if not previously adequately vaccinated. Number of doses dependent on age at initial vaccination:
    Age 9–14 years at initiation: 2-dose series at 0 and 6–12 months. Minimum interval: 5 months (repeat a dose given too soon at least 12 weeks after the invalid dose and at least 5 months after the 1st dose).
    Age 15 years or older at initiation: 3-dose series at 0, 1–2, and 6 months. Minimum intervals: 4 weeks between 1st and 2nd dose; 12 weeks between 2nd and 3rd dose; 5 months between 1st and 3rd dose (repeat dose(s) given too soon at or after the minimum interval since the most recent dose).
    Persons who have completed a valid series with any HPV vaccine do not need any additional doses.
    Special situations:

    History of sexual abuse or assault: Begin series at age 9 years.
    Immunocompromised* (including HIV) aged 9–26 years: 3-dose series at 0, 1–2, and 6 months.
    Pregnancy: Vaccination not recommended, but there is no evidence the vaccine is harmful. No intervention is needed for women who inadvertently received a dose of HPV vaccine while pregnant. Delay remaining doses until after pregnancy. Pregnancy testing not needed before vaccination.
    *See MMWR, December 16, 2016;65(49):1405–1408, at www.cdc.gov/mmwr/volumes/65/wr/pdfs/mm6549a5.pdf[4 pages].
    """
    ]
    ("Meningococcal B", None,"IM"),
    """
    Serogroup B meningococcal vaccines (minimum age: 10 years [Bexsero, Trumenba].Clinical discretion: Adolescents not at increased risk for meningococcal B infection who want MenB vaccine.MenB vaccines may be given at clinical discretion to adolescents 16–23 years (preferred age 16–18 years) who are not at increased risk.
    Bexsero: 2 doses at least 1 month apart.
    Trumenba: 2 doses at least 6 months apart. If the 2nd dose is given earlier than 6 months, give a 3rd dose at least 4 months after the 2nd.
    Special populations and situations:

    Anatomic or functional asplenia, sickle cell disease, persistent complement component deficiency (including eculizumab use), serogroup B meningococcal disease outbreak:

    Bexsero: 2-dose series at least 1 month apart.
    Trumenba: 3-dose series at 0, 1-2, and 6 months.
    Note: Bexsero and Trumenba are not interchangeable.

    For additional meningococcal vaccination information, see meningococcal MMWR publications at: www.cdc.gov/vaccines/hcp/acip-recs/vacc-specific/mening.html.
    """
    "Pneumococcal polysaccharide": ["PPSV23","IM"."CH"],
    """
    Pneumococcal vaccines. (minimum age: 6 weeks [PCV13], 2 years [PPSV23])
    Routine vaccination:

    4-dose series at 2, 4, 6, and 12–15 months.
    Catch-up vaccination with PCV13:

    1 dose for healthy children aged 24–59 months with any incomplete* PCV13 schedule
    For other catch–up guidance, see catch–up schedule.

    Special situations: High-risk conditions:

    Administer PCV13 doses before PPSV23 if possible.

    Chronic heart disease (particularly cyanotic congenital heart disease and cardiac failure); chronic lung disease (including asthma treated with high-dose, oral, corticosteroids); diabetes mellitus:

    Age 2–5 years:
    Any incomplete* schedules with:
    3 PCV13 doses: 1 dose of PCV13 (at least 8 weeks after any prior PCV13 dose).
    <3 PCV13 doses: 2 doses of PCV13, 8 weeks after the most recent dose and given 8 weeks apart.
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose).
    Age 6–18 years:
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose).
    Cerebrospinal fluid leak; cochlear implant:

    Age 2–5 years:
    Any incomplete* schedules with:
    3 PCV13 doses: 1 dose of PCV13 (at least 8 weeks after any prior PCV13 dose).
    <3 PCV13 doses: 2 doses of PCV13, 8 weeks after the most recent dose and given 8 weeks apart.
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose).
    Age 6–18 years:
    No history of either PCV13 or PPSV23: 1 dose of PCV13, 1 dose of PPSV23 at least 8 weeks later.
    Any PCV13 but no PPSV23: 1 dose of PPSV23 at least 8 weeks after the most recent dose of PCV13.
    PPSV23 but no PCV13: 1 dose of PCV13 at least 8 weeks after the most recent dose of PPSV23.
    Sickle cell disease and other hemoglobinopathies; anatomic or functional asplenia; congenital or acquired immunodeficiency; HIV infection; chronic renal failure; nephrotic syndrome; malignant neoplasms, leukemias, lymphomas, Hodgkin disease, and other diseases associated with treatment with immunosuppressive drugs or radiation therapy; solid organ transplantation; multiple myeloma:

    Age 2–5 years:
    Any incomplete* schedules with:
    3 PCV13 doses: 1 dose of PCV13 (at least 8 weeks after any prior PCV13 dose).
    <3 PCV13 doses: 2 doses of PCV13, 8 weeks after the most recent dose and given 8 weeks apart.
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose) and a 2nd dose of PPSV23 5 years later.
    Age 6–18 years:
    No history of either PCV13 or PPSV23: 1 dose of PCV13, 2 doses of PPSV23 (1st dose of PPSV23 administered 8 weeks after PCV13 and 2nd dose of PPSV23 administered at least 5 years after the 1st dose of PPSV23).
    Any PCV13 but no PPSV23: 2 doses of PPSV23 (1st dose of PPSV23 to be given 8 weeks after the most recent dose of PCV13 and 2nd dose of PPSV23 administered at least 5 years after the 1st dose of PPSV23).
    PPSV23 but no PCV13: 1 dose of PCV13 at least 8 weeks after the most recent PPSV23 dose and a 2nd dose of PPSV23 to be given 5 years after the 1st dose of PPSV23 and at least 8 weeks after a dose of PCV13.
    Chronic liver disease, alcoholism:

    Age 6–18 years:
    No history of PPSV23: 1 dose of PPSV23 (at least 8 weeks after any prior PCV13 dose).
    *Incomplete schedules are any schedules where PCV13 doses have not been completed according to ACIP recommended catch-up schedules. The total number and timing of doses for complete PCV13 series are dictated by the age at first vaccination. See Tables 8 and 9 in the ACIP pneumococcal vaccine recommendations (www.cdc.gov/mmwr/pdf/rr/rr5911.pdf[24 pages]) for complete schedule details.
    """
