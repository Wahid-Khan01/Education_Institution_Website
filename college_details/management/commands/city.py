from django.core.management.base import BaseCommand
from college_details.models import IndiaCities

class Command(BaseCommand):
    help = 'Populate Indian Cities'

    def handle(self, *args, **kwargs):
        cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 'Pune', 'Ahmedabad', 'Surat', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Patna', 'Indore', 'Thane', 'Bhopal', 'Visakhapatnam', 'Vadodara', 'Nashik', 'Faridabad', 'Ghaziabad', 'Rajkot', 'Meerut', 'Varanasi', 'Amritsar', 'Allahabad', 'Jabalpur', 'Srinagar', 'Dhanbad', 'Aurangabad', 'Ranchi', 'Howrah', 'Coimbatore', 'Gwalior', 'Vijayawada', 'Jodhpur', 'Madurai', 'Raipur', 'Kota', 'Guwahati', 'Chandigarh', 'Solapur', 'Hubballi-Dharwad', 'Bareilly', 'Moradabad', 'Mysore', 'Gurgaon', 'Aligarh', 'Jalandhar', 'Tiruchirappalli', 'Bhubaneswar', 'Salem', 'Mira-Bhayandar', 'Warangal', 'Thiruvananthapuram', 'Bhiwandi', 'Saharanpur', 'Gorakhpur', 'Guntur', 'Bikaner', 'Amravati', 'Noida', 'Jamshedpur', 'Bhilai', 'Cuttack', 'Firozabad', 'Kochi', 'Nellore', 'Bhavnagar', 'Dehradun', 'Durgapur', 'Asansol', 'Rourkela', 'Nanded', 'Kolhapur', 'Ajmer', 'Akola', 'Gulbarga', 'Jamnagar', 'Ujjain', 'Loni', 'Siliguri', 'Jhansi', 'Ulhasnagar', 'Jammu', 'Sangli-Miraj & Kupwad', 'Mangalore', 'Erode', 'Belgaum', 'Kurnool', 'Ambattur', 'Rajahmundry', 'Tirunelveli', 'Malegaon', 'Gaya', 'Jalgaon', 'Udaipur', 'Maheshtala', 'Tumkur', 'Shimla', 'Darbhanga', 'Tiruppur', 'Kollam', 'Kakinada', 'Davanagere', 'Kozhikode', 'Akbarpur', 'Satna', 'Muzaffarpur', 'Kurnool', 'Mathura', 'Gandhinagar', 'Patiala', 'Bharatpur', 'Shivamogga', 'Chandrapur', 'Port Blair', 'Adoni', 'Amaravati', 'Anantapur', 'Chandragiri', 'Chittoor', 'Dowlaiswaram', 'Eluru', 'Kadapa', 'Machilipatnam', 'Nagarjunakoṇḍa', 'Srikakulam', 'Tirupati', 'Vizianagaram', 'Yemmiganur', 'Itanagar', 'Dhuburi', 'Dibrugarh', 'Dispur', 'Jorhat', 'Nagaon', 'Sivasagar', 'Silchar', 'Tezpur', 'Tinsukia', 'Ara', 'Barauni', 'Begusarai', 'Bettiah', 'Bhagalpur', 'Bihar Sharif', 'Bodh Gaya', 'Buxar', 'Chapra', 'Dehri', 'Dinapur Nizamat', 'Hajipur', 'Jamalpur', 'Katihar', 'Madhubani', 'Motihari', 'Munger', 'Purnia', 'Pusa', 'Saharsa', 'Samastipur', 'Sasaram', 'Sitamarhi', 'Siwan', 'Ambikapur', 'Bilaspur', 'Dhamtari', 'Durg', 'Jagdalpur', 'Rajnandgaon', 'Daman', 'Diu', 'Silvassa', 'New Delhi', 'Madgaon', 'Panaji', 'Ahmadabad', 'Amreli', 'Bharuch', 'Bhuj', 'Dwarka', 'Godhra', 'Junagadh', 'Kandla', 'Khambhat', 'Kheda', 'Mahesana', 'Morbi', 'Nadiad', 'Navsari', 'Okha', 'Palanpur', 'Patan', 'Porbandar', 'Surendranagar', 'Valsad', 'Veraval', 'Ambala', 'Bhiwani', 'Firozpur Jhirka', 'Gurugram', 'Hansi', 'Hisar', 'Jind', 'Kaithal', 'Karnal', 'Kurukshetra', 'Panipat', 'Pehowa', 'Rewari', 'Rohtak', 'Sirsa', 'Sonipat', 'Chamba', 'Dalhousie', 'Dharmshala', 'Hamirpur', 'Kangra', 'Kullu', 'Mandi', 'Nahan', 'Una', 'Anantnag', 'Baramula', 'Doda', 'Gulmarg', 'Kathua', 'Punch', 'Rajouri', 'Udhampur', 'Bokaro', 'Chaibasa', 'Deoghar', 'Dumka', 'Giridih', 'Hazaribag', 'Jharia', 'Rajmahal', 'Saraikela', 'Badami', 'Ballari', 'Belagavi', 'Bhadravati', 'Bidar', 'Chikkamagaluru', 'Chitradurga', 'Davangere', 'Halebid', 'Hassan', 'Kalaburagi', 'Kolar', 'Madikeri', 'Mandya', 'Mangaluru', 'Mysuru', 'Raichur', 'Shravanabelagola', 'Shrirangapattana', 'Tumakuru', 'Vijayapura', 'Alappuzha', 'Vatakara', 'Idukki', 'Kannur', 'Kottayam', 'Mattancheri', 'Palakkad', 'Thalassery', 'Thrissur', 'Kargil', 'Leh', 'Balaghat', 'Barwani', 'Betul', 'Bharhut', 'Bhind', 'Bhojpur', 'Burhanpur', 'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dr. Ambedkar Nagar (Mhow)', 'Guna', 'Hoshangabad', 'Itarsi', 'Jhabua', 'Khajuraho', 'Khandwa', 'Khargone', 'Maheshwar', 'Mandla', 'Mandsaur', 'Morena', 'Murwara', 'Narsimhapur', 'Narsinghgarh', 'Narwar', 'Neemuch', 'Nowgong', 'Orchha', 'Panna', 'Raisen', 'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Sarangpur', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri', 'Vidisha', 'Ahmadnagar', 'Bhandara', 'Bhusawal', 'Bid', 'Buldhana', 'Daulatabad', 'Dhule', 'Kalyan', 'Karli', 'Mahabaleshwar', 'Matheran', 'Osmanabad', 'Pandharpur', 'Parbhani', 'Ratnagiri', 'Sangli', 'Satara', 'Sevagram', 'Vasai-Virar', 'Wardha', 'Yavatmal', 'Imphal']

        for city_name in cities:
            IndiaCities.objects.create(name=city_name)