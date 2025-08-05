#!/usr/bin/env python
"""
Load proper case study data with correct image mappings.
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

from casestudy.models import Casestudy, Client, Location, Industry

def load_case_studies():
    """Load case studies that match the available images."""
    
    # Clear existing data first
    print("🧹 Clearing existing case studies...")
    Casestudy.objects.all().delete()
    
    # Define case studies that match your images
    case_studies_data = [
        {
            'title': 'Floating Roof Tank System',
            'slug': 'floating-roof-tank-system',
            'image': 'floating-roof.png',
            'client': 'Petrochemical Corp',
            'location': 'Texas, USA',
            'industry': 'Oil & Gas',
            'description': 'Design and installation of floating roof tank systems for petroleum storage with advanced safety features and environmental protection.',
            'excerpt': 'Advanced floating roof tank system for safe petroleum storage.'
        },
        {
            'title': 'Fire and Gas Detection System',
            'slug': 'fire-gas-detection-system',
            'image': 'Fire-Gas-Detection.png',
            'client': 'Industrial Safety Inc',
            'location': 'Alberta, Canada',
            'industry': 'Industrial Safety',
            'description': 'Comprehensive fire and gas detection system with state-of-the-art sensors and automated response protocols.',
            'excerpt': 'Comprehensive fire and gas detection system for industrial facilities.'
        },
        {
            'title': 'Emergency Drainage and Venting System',
            'slug': 'emergency-drainage-venting-system',
            'image': 'Emergency-Drainage-Venting-System.png',
            'client': 'Chemical Processing Ltd',
            'location': 'Louisiana, USA',
            'industry': 'Chemical Processing',
            'description': 'Emergency drainage and venting system designed for chemical processing facilities to ensure safe operations.',
            'excerpt': 'Emergency drainage and venting system for chemical processing safety.'
        },
        {
            'title': 'Hazardous Waste Neutralization Unit',
            'slug': 'hazardous-waste-neutralization-unit',
            'image': 'hazardous-waste-neutralization-unit.png',
            'client': 'Environmental Solutions',
            'location': 'California, USA',
            'industry': 'Environmental',
            'description': 'Advanced hazardous waste neutralization unit for safe treatment and disposal of industrial waste materials.',
            'excerpt': 'Advanced hazardous waste neutralization and treatment facility.'
        },
        {
            'title': 'Iron Ore Pelletizing Plant',
            'slug': 'iron-ore-pelletizing-plant',
            'image': 'iron-ore-pelletizing.png',
            'client': 'Mining Consortium',
            'location': 'Minnesota, USA',
            'industry': 'Mining',
            'description': 'Large-scale iron ore pelletizing plant with automated systems for high-efficiency mineral processing.',
            'excerpt': 'Large-scale iron ore pelletizing plant with automated processing.'
        },
        {
            'title': 'Electric Arc Furnace Expansion Project',
            'slug': 'electric-arc-furnace-expansion',
            'image': 'electric-arc-furnace-eaf-expansion-project.png',
            'client': 'Steel Manufacturing Co',
            'location': 'Pennsylvania, USA',
            'industry': 'Steel Manufacturing',
            'description': 'Electric arc furnace expansion project to increase steel production capacity with energy-efficient technologies.',
            'excerpt': 'Electric arc furnace expansion for increased steel production capacity.'
        },
        {
            'title': 'Tailings Reprocessing Facility',
            'slug': 'tailings-reprocessing-facility',
            'image': 'Tailings-Reprocessing.png',
            'client': 'Mining Recovery Inc',
            'location': 'British Columbia, Canada',
            'industry': 'Mining',
            'description': 'Tailings reprocessing facility for recovery of valuable minerals from mining waste materials.',
            'excerpt': 'Tailings reprocessing facility for valuable mineral recovery.'
        },
        {
            'title': 'Solid Waste Processing Plant',
            'slug': 'solid-waste-processing-plant',
            'image': 'solid-waste-processing-plant.png',
            'client': 'Waste Management Corp',
            'location': 'Florida, USA',
            'industry': 'Waste Management',
            'description': 'Modern solid waste processing plant with recycling capabilities and energy recovery systems.',
            'excerpt': 'Modern solid waste processing plant with recycling and energy recovery.'
        },
        {
            'title': 'Skid-Mounted Process Plant',
            'slug': 'skid-mounted-process-plant',
            'image': 'skid-mounted-process-plant.png',
            'client': 'Modular Engineering',
            'location': 'Houston, Texas',
            'industry': 'Process Engineering',
            'description': 'Skid-mounted process plant for rapid deployment and flexible industrial processing applications.',
            'excerpt': 'Skid-mounted process plant for rapid deployment and flexibility.'
        },
        {
            'title': 'Renewable Energy Microgrid',
            'slug': 'renewable-energy-microgrid',
            'image': 'renewable-energy-microgrid.png',
            'client': 'Green Energy Systems',
            'location': 'Colorado, USA',
            'industry': 'Renewable Energy',
            'description': 'Renewable energy microgrid system combining solar, wind, and battery storage for sustainable power generation.',
            'excerpt': 'Renewable energy microgrid with solar, wind, and battery storage.'
        },
        {
            'title': 'Modular Carbon Capture Unit',
            'slug': 'modular-carbon-capture-unit',
            'image': 'modular-carbon-capture-utilization-ccu-unit.png',
            'client': 'Carbon Solutions Ltd',
            'location': 'Alberta, Canada',
            'industry': 'Environmental Technology',
            'description': 'Modular carbon capture and utilization unit for reducing industrial carbon emissions and climate impact.',
            'excerpt': 'Modular carbon capture and utilization unit for emission reduction.'
        }
    ]
    
    # Create or get clients, locations, and industries
    for cs_data in case_studies_data:
        client, _ = Client.objects.get_or_create(client=cs_data['client'])
        location, _ = Location.objects.get_or_create(location=cs_data['location'])
        industry, _ = Industry.objects.get_or_create(industry=cs_data['industry'])
        
        # Create case study
        casestudy = Casestudy.objects.create(
            title=cs_data['title'],
            slug=cs_data['slug'],
            client=client,
            location=location,
            industry=industry,
            description=cs_data['description'],
            excerpt=cs_data['excerpt'],
            casestudyimage=cs_data['image']
        )
        
        print(f"✓ Created: {casestudy.title} -> {casestudy.casestudyimage}")
    
    print(f"\n🎉 Successfully loaded {Casestudy.objects.count()} case studies!")

if __name__ == "__main__":
    load_case_studies()
