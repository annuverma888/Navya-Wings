from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (replace with a database or more robust data source)
success_stories = [
    {
        'name': 'Kalpana Saroj',
        'image': 'kalpana_saroj.jpg',  # Replace with actual image path
        'story': 'From a child bride to a successful entrepreneur, Kalpana Saroj defied all odds to build a multi-million dollar business.',
        'category': 'Entrepreneurship'
    },
    {
        'name': 'Tessy Thomas',
        'image': 'tessy_thomas.jpg', # Replace with actual image path
        'story': 'Known as the "Missile Woman of India," Tessy Thomas led the Agni-IV missile project, proving that women can excel in science and technology.',
        'category': 'Science & Technology'
    },
    {
        'name': 'Mithali Raj',
        'image': 'mithali_raj.jpg', # Replace with actual image path
        'story': 'A legendary cricketer, Mithali Raj has inspired countless girls to pursue their dreams in sports, breaking barriers and setting records.',
        'category': 'Sports'
    },
    # Add more success stories here
]

business_guidance = [
    {
        'title': 'Starting a Small Tailoring Business',
        'content': 'Learn about the tools, materials, and basic techniques needed to start a tailoring business. Get tips on marketing and managing your finances.',
        'resources': ['Link to a tailoring tutorial', 'Link to a small business resource']
    },
    {
        'title': 'Poultry Farming Basics',
        'content': 'Information about setting up a small poultry farm, including choosing breeds, feeding, and disease prevention. Learn how to market your products.',
        'resources': ['Link to a poultry farming guide', 'Link to a government agriculture website']
    },
    # Add more business guidance topics
]

health_information = [
    {
        'title': 'Menstrual Hygiene Management',
        'content': 'Information about proper menstrual hygiene, including the use of sanitary products, hygiene practices, and addressing common myths.',
        'resources': ['Link to a menstrual hygiene resource', 'Link to a local health organization']
    },
        {
        'title': 'Nutrition for adolescent girls',
        'content': 'Information about the importance of balanced diet for adolescent girls',
        'resources': ['Link to a nutrition resource', 'Link to a local health organization']
    },
    # Add more health information topics
]

career_guidance = [
    {
        'title': 'Choosing a Career Path',
        'content': 'Tips for identifying your interests and skills, exploring different career options, and setting career goals. Learn about educational requirements and job market trends.',
        'resources': ['Link to a career counseling resource', 'Link to a skills development website']
    },
        {
        'title': 'Interview Skills',
        'content': 'Tips for preparing for job interviews',
        'resources': ['Link to an interview skills resource', 'Link to a local career center']
    },
    # Add more career guidance topics
]

@app.route('/')
def home():
    return render_template('index.html', stories=success_stories)

@app.route('/business')
def business():
    return render_template('business.html', guidance=business_guidance)

@app.route('/health')
def health():
    return render_template('health.html', health_info=health_information)

@app.route('/career')
def career():
    return render_template('career.html', career_info=career_guidance)

if __name__ == '__main__':
    app.run(debug=True)