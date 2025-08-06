from django.core.management.base import BaseCommand
from casestudy.models import Casestudy, Client, Location, Industry


class Command(BaseCommand):
    help = 'Load case study data for production deployment'

    def handle(self, *args, **options):
        self.stdout.write('🧹 Clearing existing case studies...')
        Casestudy.objects.all().delete()
        
        # Professional case study data with proper image mappings
        case_studies_data = [
            {
                'title': 'Electric Arc Furnace (EAF) Expansion Project',
                'slug': 'electric-arc-furnace-eaf-expansion-project',
                'client': 'SteelTech Industries',
                'location': 'Birmingham, United Kingdom', 
                'industry': 'Steel Manufacturing',
                'description': '''<p>SteelTech Industries approached CoreFlow EPC to expand their existing electric arc furnace capacity to meet growing demand for high-quality steel products. The project involved designing and constructing a state-of-the-art 150-ton EAF facility with advanced automation systems.</p>
                
                <p><strong>Key Challenges:</strong></p>
                <ul>
                    <li>Limited space for expansion within existing facility</li>
                    <li>Maintaining production during construction</li>
                    <li>Meeting strict environmental regulations</li>
                    <li>Integrating with legacy systems</li>
                </ul>
                
                <p><strong>Solution Delivered:</strong></p>
                <ul>
                    <li>Modular design approach to minimize downtime</li>
                    <li>Advanced dust collection and emission control systems</li>
                    <li>Automated charging system with robotic material handling</li>
                    <li>Energy recovery systems reducing operating costs by 25%</li>
                </ul>
                
                <p><strong>Results:</strong> The project was completed on schedule and 5% under budget, increasing production capacity by 60% while reducing energy consumption per ton of steel by 30%.</p>''',
                'excerpt': 'State-of-the-art 150-ton electric arc furnace expansion with advanced automation and energy recovery systems.',
                'image': 'electric-arc-furnace-eaf-expansion-project.png'
            },
            {
                'title': 'Tailings Reprocessing Facility',
                'slug': 'tailings-reprocessing-facility', 
                'client': 'MineraCorp',
                'location': 'Perth, Australia',
                'industry': 'Mining & Minerals',
                'description': '''<p>MineraCorp engaged CoreFlow EPC to design and construct a comprehensive tailings reprocessing facility to extract valuable minerals from historical mine tailings while addressing environmental remediation requirements.</p>
                
                <p><strong>Project Scope:</strong></p>
                <ul>
                    <li>Processing capacity: 2,000 tonnes per day</li>
                    <li>Recovery of copper, gold, and rare earth elements</li>
                    <li>Water recycling and treatment systems</li>
                    <li>Automated material handling and processing</li>
                </ul>
                
                <p><strong>Environmental Benefits:</strong></p>
                <ul>
                    <li>Remediation of 50 hectares of contaminated land</li>
                    <li>90% water recycling rate</li>
                    <li>Reduction of acid mine drainage</li>
                    <li>Creation of 150 permanent jobs</li>
                </ul>
                
                <p><strong>Technology Integration:</strong> Advanced flotation circuits, magnetic separation, and hydrometallurgical processing with real-time monitoring and control systems.</p>''',
                'excerpt': 'Innovative tailings reprocessing facility combining mineral recovery with environmental remediation.',
                'image': 'Tailings-Reprocessing.png'
            },
            {
                'title': 'Iron Ore Pelletizing Plant',
                'slug': 'iron-ore-pelletizing-plant',
                'client': 'Nordic Iron AB',
                'location': 'Kiruna, Sweden',
                'industry': 'Mining & Minerals', 
                'description': '''<p>Nordic Iron AB commissioned CoreFlow EPC to design and construct a modern iron ore pelletizing plant to produce high-quality pellets for the European steel industry, focusing on efficiency and environmental sustainability.</p>
                
                <p><strong>Plant Specifications:</strong></p>
                <ul>
                    <li>Annual capacity: 5 million tonnes of pellets</li>
                    <li>Grate-kiln pelletizing technology</li>
                    <li>Waste heat recovery systems</li>
                    <li>Advanced process control and optimization</li>
                </ul>
                
                <p><strong>Innovation Highlights:</strong></p>
                <ul>
                    <li>Energy-efficient induration process reducing fuel consumption by 20%</li>
                    <li>Selective catalytic reduction (SCR) for NOx emission control</li>
                    <li>Automated quality control with online analyzers</li>
                    <li>Digital twin technology for process optimization</li>
                </ul>
                
                <p><strong>Sustainability Features:</strong> The plant incorporates renewable energy sources, achieving carbon neutrality in pellet production through biomass co-firing and waste heat utilization.</p>''',
                'excerpt': 'Modern iron ore pelletizing plant with advanced environmental controls and energy efficiency systems.',
                'image': 'iron-ore-pelletizing.png'
            },
            {
                'title': 'Emergency Drainage & Venting System',
                'slug': 'emergency-drainage-venting-system',
                'client': 'ChemSecure Ltd',
                'location': 'Rotterdam, Netherlands',
                'industry': 'Chemical Processing',
                'description': '''<p>ChemSecure Ltd required a comprehensive emergency drainage and venting system for their chemical storage and processing facility to ensure safe handling of hazardous materials and compliance with international safety standards.</p>
                
                <p><strong>System Components:</strong></p>
                <ul>
                    <li>Emergency relief valve systems</li>
                    <li>Automated drainage networks</li>
                    <li>Vapor containment and treatment units</li>
                    <li>Emergency response integration systems</li>
                </ul>
                
                <p><strong>Safety Features:</strong></p>
                <ul>
                    <li>Fail-safe operation with redundant systems</li>
                    <li>Real-time monitoring and alarm systems</li>
                    <li>Integration with plant-wide safety systems</li>
                    <li>Emergency response protocol automation</li>
                </ul>
                
                <p><strong>Compliance:</strong> The system meets ATEX, SEVESO III, and local Dutch safety regulations, with third-party verification and certification completed successfully.</p>''',
                'excerpt': 'Comprehensive emergency safety system for chemical processing facility with automated response capabilities.',
                'image': 'Emergency-Drainage-Venting-System.png'
            },
            {
                'title': 'Fire & Gas Detection Network',
                'slug': 'fire-gas-detection-network',
                'client': 'PetroSafe International',
                'location': 'Abu Dhabi, UAE',
                'industry': 'Oil & Gas',
                'description': '''<p>PetroSafe International engaged CoreFlow EPC to design and install a state-of-the-art fire and gas detection system for their offshore processing platform, ensuring maximum safety for personnel and equipment protection.</p>
                
                <p><strong>Detection Capabilities:</strong></p>
                <ul>
                    <li>Multi-spectrum flame detection</li>
                    <li>Toxic and combustible gas monitoring</li>
                    <li>Heat detection with thermal imaging</li>
                    <li>Smoke detection in enclosed areas</li>
                </ul>
                
                <p><strong>Advanced Features:</strong></p>
                <ul>
                    <li>Wireless sensor networks for hard-to-reach areas</li>
                    <li>AI-powered false alarm reduction</li>
                    <li>Integration with emergency shutdown systems</li>
                    <li>Real-time data transmission to control room</li>
                </ul>
                
                <p><strong>Performance:</strong> The system provides 99.9% uptime with response times under 2 seconds, significantly enhancing platform safety and reducing insurance premiums by 15%.</p>''',
                'excerpt': 'Advanced fire and gas detection system for offshore platform with AI-powered monitoring and response.',
                'image': 'Fire-Gas-Detection.png'
            },
            {
                'title': 'Floating Roof Storage System',
                'slug': 'floating-roof-storage-system',
                'client': 'Global Energy Storage Corp',
                'location': 'Houston, Texas, USA',
                'industry': 'Oil & Gas',
                'description': '''<p>Global Energy Storage Corp commissioned CoreFlow EPC to design and construct a series of floating roof storage tanks for their strategic petroleum reserve facility, focusing on product integrity and environmental protection.</p>
                
                <p><strong>Tank Specifications:</strong></p>
                <ul>
                    <li>Six tanks with 100,000 barrel capacity each</li>
                    <li>External floating roof design</li>
                    <li>Advanced sealing systems</li>
                    <li>Automated level monitoring and control</li>
                </ul>
                
                <p><strong>Environmental Protection:</strong></p>
                <ul>
                    <li>Vapor emission reduction by 95%</li>
                    <li>Secondary containment systems</li>
                    <li>Groundwater monitoring wells</li>
                    <li>Automated leak detection systems</li>
                </ul>
                
                <p><strong>Innovation:</strong> Smart roof position monitoring with predictive maintenance algorithms, reducing maintenance costs by 30% while ensuring optimal product quality preservation.</p>''',
                'excerpt': 'Large-capacity floating roof storage tanks with advanced environmental protection and monitoring systems.',
                'image': 'floating-roof.png'
            },
            {
                'title': 'Hazardous Waste Neutralization Unit',
                'slug': 'hazardous-waste-neutralization-unit',
                'client': 'EcoTreat Solutions',
                'location': 'Frankfurt, Germany',
                'industry': 'Environmental Services',
                'description': '''<p>EcoTreat Solutions partnered with CoreFlow EPC to develop a mobile hazardous waste neutralization unit capable of treating various chemical wastes on-site, reducing transportation risks and treatment costs.</p>
                
                <p><strong>Treatment Capabilities:</strong></p>
                <ul>
                    <li>Acid and alkaline waste neutralization</li>
                    <li>Heavy metal precipitation and removal</li>
                    <li>Organic compound destruction</li>
                    <li>Solidification of treated residues</li>
                </ul>
                
                <p><strong>Mobile Design Features:</strong></p>
                <ul>
                    <li>Truck-mounted processing equipment</li>
                    <li>Self-contained utilities and controls</li>
                    <li>Rapid deployment capability (2-hour setup)</li>
                    <li>Remote monitoring and control systems</li>
                </ul>
                
                <p><strong>Environmental Impact:</strong> The unit has successfully treated over 10,000 tonnes of hazardous waste, achieving 99.5% treatment efficiency while reducing carbon footprint by 60% compared to traditional off-site treatment.</p>''',
                'excerpt': 'Mobile hazardous waste treatment unit providing on-site neutralization and remediation services.',
                'image': 'hazardous-waste-neutralization-unit.png'
            },
            {
                'title': 'Solid Waste Processing Plant',
                'slug': 'solid-waste-processing-plant',
                'client': 'Metro Waste Management',
                'location': 'Toronto, Canada',
                'industry': 'Environmental Services',
                'description': '''<p>Metro Waste Management selected CoreFlow EPC to design and construct a state-of-the-art solid waste processing facility incorporating advanced sorting, recycling, and energy recovery technologies to achieve zero-landfill goals.</p>
                
                <p><strong>Processing Capacity:</strong></p>
                <ul>
                    <li>500 tonnes per day municipal solid waste</li>
                    <li>Automated sorting and separation systems</li>
                    <li>Material recovery facility (MRF)</li>
                    <li>Refuse-derived fuel (RDF) production</li>
                </ul>
                
                <p><strong>Technology Integration:</strong></p>
                <ul>
                    <li>AI-powered optical sorting systems</li>
                    <li>Magnetic and eddy current separators</li>
                    <li>Ballistic separation technology</li>
                    <li>Quality control and contamination detection</li>
                </ul>
                
                <p><strong>Sustainability Results:</strong> The facility achieves 85% waste diversion from landfills, produces 50 MWh of renewable energy daily, and creates 75 local jobs while reducing municipal waste management costs by 40%.</p>''',
                'excerpt': 'Advanced waste processing facility with AI-powered sorting and energy recovery achieving 85% waste diversion.',
                'image': 'solid-waste-processing-plant.png'
            },
            {
                'title': 'Skid-Mounted Process Plant',
                'slug': 'skid-mounted-process-plant',
                'client': 'FlexiChem Industries',
                'location': 'Singapore',
                'industry': 'Chemical Processing',
                'description': '''<p>FlexiChem Industries required a flexible, modular chemical processing solution that could be rapidly deployed and reconfigured for different product campaigns. CoreFlow EPC delivered a comprehensive skid-mounted system meeting these demanding requirements.</p>
                
                <p><strong>Modular Design:</strong></p>
                <ul>
                    <li>Pre-fabricated process modules</li>
                    <li>Plug-and-play interconnections</li>
                    <li>Scalable processing capacity</li>
                    <li>Mobile control room integration</li>
                </ul>
                
                <p><strong>Process Capabilities:</strong></p>
                <ul>
                    <li>Multi-product batch processing</li>
                    <li>Automated recipe management</li>
                    <li>CIP (Clean-in-Place) systems</li>
                    <li>Quality control and batch tracking</li>
                </ul>
                
                <p><strong>Operational Benefits:</strong> The modular design reduces setup time by 70%, enables rapid product changeovers, and provides 99.8% uptime with predictive maintenance capabilities.</p>''',
                'excerpt': 'Flexible skid-mounted chemical processing system with modular design and rapid deployment capabilities.',
                'image': 'skid-mounted-process-plant.png'
            },
            {
                'title': 'Renewable Energy Microgrid',
                'slug': 'renewable-energy-microgrid',
                'client': 'Island Power Solutions',
                'location': 'Orkney Islands, Scotland',
                'industry': 'Renewable Energy',
                'description': '''<p>Island Power Solutions commissioned CoreFlow EPC to design and construct a renewable energy microgrid system to provide sustainable power for the remote Orkney Islands community, reducing dependence on fossil fuels and improving energy security.</p>
                
                <p><strong>System Components:</strong></p>
                <ul>
                    <li>5 MW wind turbine installation</li>
                    <li>2 MW solar photovoltaic array</li>
                    <li>Battery energy storage system (10 MWh)</li>
                    <li>Smart grid control and management</li>
                </ul>
                
                <p><strong>Grid Integration:</strong></p>
                <ul>
                    <li>Islanding capability for energy independence</li>
                    <li>Grid-tie functionality for surplus export</li>
                    <li>Load balancing and demand response</li>
                    <li>Weather prediction and generation forecasting</li>
                </ul>
                
                <p><strong>Community Impact:</strong> The microgrid provides 95% renewable energy, reduces electricity costs by 45%, and serves as a model for other remote communities seeking energy independence.</p>''',
                'excerpt': 'Comprehensive renewable energy microgrid providing sustainable power for remote island community.',
                'image': 'renewable-energy-microgrid.png'
            },
            {
                'title': 'Modular Carbon Capture Utilization (CCU) Unit',
                'slug': 'modular-carbon-capture-utilization-ccu-unit',
                'client': 'CarbonTech Innovations',
                'location': 'Calgary, Canada',
                'industry': 'Renewable Energy',
                'description': '''<p>CarbonTech Innovations partnered with CoreFlow EPC to develop a modular carbon capture and utilization system that converts industrial CO2 emissions into valuable chemical feedstocks, supporting circular economy principles.</p>
                
                <p><strong>Capture Technology:</strong></p>
                <ul>
                    <li>Post-combustion CO2 capture</li>
                    <li>Advanced solvent-based absorption</li>
                    <li>95% capture efficiency</li>
                    <li>Processing capacity: 1,000 tonnes CO2/day</li>
                </ul>
                
                <p><strong>Utilization Processes:</strong></p>
                <ul>
                    <li>CO2 to methanol conversion</li>
                    <li>Synthetic fuel production</li>
                    <li>Chemical feedstock generation</li>
                    <li>Enhanced oil recovery applications</li>
                </ul>
                
                <p><strong>Environmental Benefits:</strong> The system prevents 300,000 tonnes of CO2 emissions annually while producing 200,000 tonnes of valuable chemical products, demonstrating commercial viability of carbon utilization technology.</p>''',
                'excerpt': 'Innovative carbon capture and utilization system converting CO2 emissions into valuable chemical products.',
                'image': 'modular-carbon-capture-utilization-ccu-unit.png'
            }
        ]
        
        self.stdout.write('🔧 Loading case study data...')
        
        for data in case_studies_data:
            try:
                # Get or create related objects
                client_obj, _ = Client.objects.get_or_create(client=data['client'])
                location_obj, _ = Location.objects.get_or_create(location=data['location'])
                industry_obj, _ = Industry.objects.get_or_create(industry=data['industry'])
                
                # Create case study (without image initially)
                casestudy = Casestudy.objects.create(
                    title=data['title'],
                    slug=data['slug'],
                    client=client_obj,
                    location=location_obj,
                    industry=industry_obj,
                    description=data['description'],
                    excerpt=data['excerpt']
                    # Note: casestudyimage will be set later by upload_cloudinary command
                )
                
                self.stdout.write(f'✓ Created: {casestudy.title} (image will be added by upload_cloudinary command)')
                
            except Exception as e:
                self.stdout.write(f'❌ Error creating {data["title"]}: {str(e)}')
        
        self.stdout.write('🎉 Case study data loading completed!')
        self.stdout.write(f'📊 Total case studies: {Casestudy.objects.count()}')
