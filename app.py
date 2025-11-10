from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Portfolio Data
portfolio_data = {
    'personal': {
        'name': 'Kashish Chopra',
        'title': 'B.Tech CSE (AIML) Student',
        'tagline': 'Passionate about coding, problem-solving, and exploring emerging technologies',
        'email': 'kashishchopra2k05@gmail.com',
        'phone': '+91 95xxx xxxxx',
        'location': 'Dwarka, New Delhi',
        'linkedin': 'linkedin.com/in/kashishchopra',
        'github': 'github.com/kashishchopra',
        'website': 'kashishchopra.dev'
    },
    'about': {
        'description': "I'm a passionate and enthusiastic B.Tech Computer Science and Engineering (AIML) student with a strong interest in coding, problem-solving, and exploring new technologies. I have a solid foundation in Python, Java, C, and C#, with knowledge of database management and modern frameworks. I'm responsible, self-motivated, and always open to feedback, aiming to apply my knowledge through practical experience and add value to real-world projects.",
        'highlights': [
            'B.Tech CSE (AIML) student at The NorthCap University',
            'Strong foundation in Python, Java, C, and C# programming',
            'Experience with modern frameworks like React, Django, Flask',
            'Internship experience at Indian Oil Corporation Limited',
            'Current CGPA: 7.48 with consistently improving performance'
        ]
    },
    'experience': [
        {
            'id': 1,
            'company': 'Indian Oil Corporation Limited',
            'position': 'Information Services (IS) Department Intern',
            'duration': 'Summer Internship',
            'location': 'New Delhi, India',
            'description': "Worked on the development of an E-Commerce Website 'Vistora' using .NET (C# framework) with comprehensive features for online retail operations.",
            'achievements': [
                'Developed complete E-Commerce platform from scratch',
                'Implemented product catalog with advanced search functionality',
                'Built shopping cart and order management system',
                'Gained hands-on experience with enterprise-level development'
            ],
            'technologies': ['.NET', 'C#', 'SQL', 'Web Development']
        },
        {
            'id': 2,
            'company': 'Academic Projects',
            'position': 'Student Developer',
            'duration': '2023 - Present',
            'location': 'The NorthCap University, Gurugram',
            'description': 'Engaged in various academic projects and assignments focused on programming fundamentals, data analysis, and software development.',
            'achievements': [
                'Consistently improved academic performance (CGPA from 6.91 to 8.32)',
                'Completed multiple programming projects in different languages',
                'Developed strong problem-solving and analytical skills',
                'Gained experience with various development tools and frameworks'
            ],
            'technologies': ['Python', 'Java', 'C', 'C#', 'React', 'Django', 'Flask']
        }
    ],
    'skills': {
        'technical': [
            {'name': 'Python', 'level': 85},
            {'name': 'Java', 'level': 80},
            {'name': 'C', 'level': 75},
            {'name': 'C#', 'level': 75},
            {'name': 'React', 'level': 70},
            {'name': 'Django', 'level': 65},
            {'name': 'Flask', 'level': 70},
            {'name': 'SQL', 'level': 75},
            {'name': '.NET', 'level': 70},
            {'name': 'Angular', 'level': 60}
        ],
        'soft': [
            'Teamwork & Collaboration',
            'Communication',
            'Adaptability',
            'Time Management',
            'Problem Solving & Design Thinking',
            'Project Management'
        ],
        'tools': [
            'VS Code', 'GitHub', 'Docker', 'MATLAB', 'SolidWorks', 'AutoCAD',
            'Jupyter Notebook', 'Pandas', 'MS Word & PowerPoint'
        ]
    },
    'education': [
        {
            'id': 1,
            'institution': 'The NorthCap University, Gurugram',
            'degree': 'B.Tech Computer Science & Engineering (AIML)',
            'duration': '2023 - 2027',
            'gpa': '7.48/10.0',
            'honors': 'Current Student',
            'details': 'Sem1: 7.38 | Sem2: 6.91 | Sem3: 7.18 | Sem4: 8.32',
            'coursework': [
                'Programming Fundamentals',
                'Data Structures & Algorithms',
                'Database Management Systems',
                'Artificial Intelligence & Machine Learning',
                'Software Engineering',
                'Computer Networks'
            ]
        },
    
    ],
    'projects': [
        {
            'id': 1,
            'name': 'E-Commerce Website - Vistora',
            'description': 'Comprehensive e-commerce platform developed during internship at Indian Oil Corporation Limited with product catalog, shopping cart, and order management features',
            'technologies': ['.NET', 'C#', 'SQL', 'Web Development'],
            'github': 'github.com/kashishchopra/vistora',
            'demo': 'vistora.demo.com'
        },
        {
            'id': 2,
            'name': 'ATM Simulation System',
            'description': 'Complete ATM simulation system with user authentication, balance inquiry, cash withdrawal, and transaction history',
            'technologies': ['Java', 'OOP Concepts', 'File Handling'],
            'github': 'github.com/kashishchopra/atm-simulation'
        },
        {
            'id': 3,
            'name': 'Motor Vehicle Data Collision Analysis',
            'description': 'Data analysis project for analyzing motor vehicle collision patterns and trends using statistical methods',
            'technologies': ['Python', 'Pandas', 'Data Analysis', 'Matplotlib'],
            'github': 'github.com/kashishchopra/vehicle-collision-analysis'
        },
        {
            'id': 4,
            'name': 'Urban Traffic Pattern Analysis',
            'description': 'Analysis of urban traffic patterns to identify congestion points and optimize traffic flow',
            'technologies': ['Python', 'Data Science', 'Statistical Analysis'],
            'github': 'github.com/kashishchopra/urban-traffic-analysis'
        },
        {
            'id': 5,
            'name': 'Comprehensive Weather Data Analysis',
            'description': 'Weather data analysis project for pattern recognition and forecasting using machine learning techniques',
            'technologies': ['Python', 'Machine Learning', 'Data Visualization'],
            'github': 'github.com/kashishchopra/weather-analysis'
        }
    ],
    'contact': {
        'availability': 'Available for internships and entry-level opportunities',
        'preferredContact': 'email',
        'responseTime': 'Usually responds within 24 hours'
    },
    'interests': {
        'hobbies': [
            'Reading non-fiction and personal development books',
            'Writing short articles/blogs',
            'Playing Badminton'
        ],
        'interests': [
            'Exploring emerging technologies and innovations',
            'Traveling and learning about diverse cultures',
            'Data Analysis and Machine Learning',
            'Graphic Designing'
        ]
    }
}

@app.route('/')
def home():
    """Main portfolio page"""
    return render_template('index.html', data=portfolio_data)

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'message': 'All fields are required'})
        
        # Here you can add email sending logic or save to database
        # For now, we'll just simulate successful submission
        
        print(f"Contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        print(f"Timestamp: {datetime.now()}")
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I\'ll get back to you within 24 hours.'
        })
        
    except Exception as e:
        print(f"Error in contact form: {e}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'})

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
