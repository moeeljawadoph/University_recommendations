# -*- coding: utf-8 -*-
"""
The file is created to include the initial parameter
"""
nsample=200

threshold = 80

def get_value_list():
    """
    Returns
    -------
    dict
        Dictionary of keys corresponding to courses and their combinations, and values as the lists of courses and their combinations
    
    
    """

    #list of fields:
    Math_Geography = ["Surveying and Geomatics", "Geographic Information Systems", "Cartography", "Metorology"]
    Math_Economy = ["Economics", "Financial Services", "Risk Manager","Quantitative Analyst"]
    Math_Chemistry =["Chemical Engineering","Analytical Chemistry","Chemical Education","Computational Chemistry"]
    Math_Biology =["Bioinformatics","Epidemiology","Biostatistics","Computational Biology"]
    Math_History =["Actuarial Science","Economic History Research","Quantitative Historical Analysis","Statistical Demography"]
    Math_English = ["Technical Writing","Data Reporting", "Math Journalism"]
    Math=["Mathematics","Data Analysis","Data Scientist","Computer Science"]
    
    
    Physics_Math =["Mathematical Modeling","Quantum Mechanics","Mathematical Physics"]
    Physics_Chemistry =["Materials Science","Chemical Engineering","Environmental Chemistry","Physical Chemistry"]
    Physics_Biology =["Biophysics","Biomedical Engineering","BioMechanics","Radiology"]
    Physics_History =["History of Physics","Philosophy of Physics","Science Education and Outreach"]
    Physics_English =["Science Writing","Technical Writing in Physics","Physics Education","Publishing and Editing in Physics"]
    Physics_Economy=["Energy Economics", "Econophysics"]
    Physics_Geography = ["Geospatial Techoology","Plantery Science", "GeoPhysics"]
    Physics =["Theortical Physics","Astrophysics","Experimental Physics","Physics Education"]
    
    
    
    Chemistry_Biology =["Biochemistry","Pharmacology","Molecular Biology"]
    Chemistry=["Analytical Chemistry","Organic Chemistry","Chemsitry Education","Inorganic Chemistry","Lab Assistant"]
    
    
    
    Biology =["Biotechnology","Microbiology","Biology Education","Medicine"]
    
    
    
    History_English =["Historical Research and Writing","Archival Studies","Digital Humanities","Cultural Heritage Preservation"]
    History_Biology =["Environmental History","Medical History","Historical Anthropology","Museum Curator"]
    History_Chemistry=[ "History of Chemical Discoveries", "Evolution of Chemical Education"]
    History_Economy =["Economic History","Economic Policy Analysis","Business and Economic Journalism"]
    History =["Museum Curator","Archivist","Journalism and Media","Government and Public Services"]
    
    
    
    English_Biology =["Journalism","Public Relations","Technical Writing","Content Management"]
    English_Chemistry = ["Technical Writing for Chemistry", "Chemistry Education and Curriculum Development"]
    English_Economy = ["Global Financial Markets","English Language Skills for Economic Forecasting"]
    English =["English Education","Journalism","Content Creation","Translation"]
    
    
    
    Economy_Chemistry = ["Economics of Chemical Manufacturing", "Chemistry and Resource Economics"]
    Economy_Biology = ["Biotechnology and Economic Development", "Economics of Biomedical Research and Development"]
    Economy =["Microeconomics","Macroeconomics","Economics and Finance"]
    
    
    
    Geography_Biology = ["Landscape Ecology and Biotic Interactions"]
    Geography_Chemistry=["Geography of Chemical Waste Management", "Spatial Dynamics of Chemical Reactions"]
    History_Geography =["Historical Geography","Archaeology"]
    Geography_English =["Travel Writing and Guidebook Publishing","Environmental Jouralism"]
    Geography_Economy =["Environmental Economics","Urban Planing and Regional Development"]
    Geography =["Transportation and Logistics","Geography Eduacation","Tourism and Hospitality"]
    
    
    
    value_lists = {'Math_Geography': Math_Geography,
                   'Math_Economy': Math_Economy,
                   'Math_Chemistry': Math_Chemistry,
                   'Math_Biology': Math_Biology,
                   'Math_History': Math_History,
    			   'Math_English':Math_English,
                   'Math': Math,
                   'Physics_Math': Physics_Math,
                   'Physics_Chemistry': Physics_Chemistry,
                   'Physics_Biology': Physics_Biology,
                   'Physics_History': Physics_History,
                   'Physics_English': Physics_English,
    			   'Physics_Economy': Physics_Economy,
    			   'Physics_Geography':Physics_Geography,
                   'Physics':Physics,
                   'Chemistry_Biology':Chemistry_Biology,
    			   'History_Chemistry':History_Chemistry,
                   'Chemistry': Chemistry,
                   'Biology':Biology,
                   'History_English':History_English,
                   'History_Biology':History_Biology,
                   'History_Economy':History_Economy,
                   'History':History,
                   'English_Biology':English_Biology,
                   'English_Chemistry':English_Chemistry,
    			   'English_Economy':English_Economy,
    			   'English':English,
    			   'Economy_Chemistry':Economy_Chemistry,
    			   'Economy_Biology':Economy_Biology,
                   'Economy':Economy,
                   'History_Geography':History_Geography,
    			   'Geography_Biology':Geography_Biology,
    			   'Geography_Chemistry':Geography_Chemistry,
                   'Geography_English':Geography_English,
                   'Geography_Economy':Geography_Economy,
                   'Geography':Geography
                   }
    return value_lists