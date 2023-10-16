# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:53:41 2023

@author: eljawadmo

The file is created to include the initial parameter
"""

#Threshold of split
threshold = 80

#
nsample = 100000

#list of fields:
Math_Geography = ["Surveying and Geomatics", "Geographic Information Systems", "Cartography", "Metorology"]
Math_Economy = ["Economics", "Financial Services", "Risk Manager","Quantitative Analyst"]
Math_Chemistry =["Chemical Engineering","Medicinal Chemistry","Analytical Chemistry","Quantum Chemistry","Chemical Education","Computational Chemistry"]
Math_Biology =["Bioinformatics","Epidemiology","Biostatistics","Computational Biology","Mathematical Biology"]
Math_History =["Actuarial Science","Economic History Research","Mathematical Archaeology","Quantitative Historical Analysis","Statistical Demography"]
Math_English = ["Technical Writing","Data Reporting", "Math Journalism"]
Math=["Mathematics","Data Analysis","Data Scientist","Computer Science","Signal Processing Engineers","Operation Resarch"]


Physics_Math =["Mathematical Modeling","Quantum Mechanics","Mathematical Physics"]
Physics_Chemistry =["Materials Science","Chemical Engineering","Environmental Chemistry","Physical Chemistry","Geochemistry","Atmospheric Chemistry"]
Physics_Biology =["Biophysics","Biomedical Engineering","BioMechanics","Medical Physics","Physiology","Radiology"]
Physics_History =["History of Physics","Philosophy of Physics","Science Education and Outreach","Historical Instrumentation and Experimental Replication","Science Communication and Writing","Historical Analysis of Technological Advances"]
Physics_English =["Science Writing","Technical Writing in Physics","Physics Journalism","Physics Education","Science Communication","Publishing and Editing in Physics","Research in Science and Technology Communication","Physics Content Creation","Science Editing","Curriculum Development"]
Physics_Economy=["Energy Economics", "econophysics"]
Physics_Geography = ["Geospatial Techoology","Plantery Science", "GeoPhysics", "Climate Science"]
Physics =["Theortical Physics","Astrophysics","Experimental Physics","Physics Education","Science Journalism"]


Chemistry_Biology =["Biochemistry","Pharmacology","Molecular Biology"]
Chemistry=["Analytical Chemistry","Organic Chemistry","Education","Inorganic Chemistry","Lab Assistant"]

Biology =["Biotechnology","Microbiology","Anatomy","Ecology","Medicine"]



History_English =["Historical Research and Writing","Archival Studies","Digital Humanities","Historiography and Criticism","Historical Journalism","Museum Curation and Interpretation","Historical Fiction Writing","Cultural Heritage Preservation","Academic Publishing","Historical Education and Outreach"]
History_Biology =["History of Science","Environmental History","Medical History","Historical Anthropology","Museum Curator","Bioarchaeology"]
History_Chemistry=["Chemistry and Scientific Revolution", "History of Chemical Discoveries", "Evolution of Chemical Education"]
History_Economy =["Economic History","Economic Policy Analysis","Financial Sector Regulatoins","Business and Economic Journalism"]
History =["Museum Curator","Archivist","Journalism and Media","Government and Public Services","Historical Preservation and Cultural Heritage"]



English_Biology =["Journalism","Public Relations","Copywriting","Publishing","Editing","Technical Writing","Education","Content Management","Digital Marketing","Creative Writing"]
English_Chemistry = ["Scientific Writing in Chemistry", "Chemistry Journalism", "Technical Writing for Chemistry", "Chemistry Education and Curriculum Development"]
English_Economy = ["Global Financial Markets","English Language Skills for Economic Forecasting"]
English =["Writing and Editing","Journalism","Public Relations","Copywriting","Content Creation","Publishing","Technical Writing","Education","Translation","Communications"]

Economy_Chemistry = ["Sustainable Chemistry and Economic Development", "Chemical Supply Chain Management", "Economics of Chemical Manufacturing", "Chemical Market Forecasting and Analysis", "Chemistry and Resource Economics", "Cost-benefit Analysis in Chemical Projects", "Economic Policies in the Chemical Sector"]
Economy_Biology = ["Biotechnology and Economic Development", "Economics of Biomedical Research and Development", "Sustainable Economics in Biology Conservation"]
Economy =["Microeconomics","Macroeconomics","Economic Policy","International Economics","Public Finance","Econometrics"]

Geography_Biology = ["Landscape Ecology and Biotic Interactions","Conservation of Biodiversity Hotspots","Geographical Perspectives on Ecosystem Services"]
Geography_Chemistry=["Geography of Chemical Waste Management", "Spatial Dynamics of Chemical Reactions"]
History_Geography =["Historical Geography","Cultural Heritage Management and Preservation","Archaeology","Academic Research and Teaching"]
Geography_English =["Academic Research","Travel Writing and Guidebook Publishing","Environmental Jouralism","Cultural Heritage Preservation"]
Geography_Economy =["International Development","Environmental Economics","Urban Planing and Regional Development"]
Geography =["Transportation and Logistics","Emergency management and Disaster","Tourism and Hospitality"]


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
