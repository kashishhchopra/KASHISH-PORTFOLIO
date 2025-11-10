# Kashish Chopra - Portfolio Website

A modern, responsive portfolio website built with Flask, HTML, CSS, and JavaScript.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with smooth animations
- **Contact Form**: Functional contact form with server-side handling
- **Fast Loading**: Optimized static files and efficient code
- **SEO Friendly**: Proper meta tags and semantic HTML structure

## Sections

- **Hero**: Eye-catching introduction with call-to-action buttons
- **About**: Personal introduction and key highlights
- **Experience**: Timeline of work experience and internships
- **Skills**: Technical skills with progress bars, soft skills, and tools
- **Projects**: Showcase of academic and personal projects
- **Education**: Educational background and coursework
- **Contact**: Contact information and working contact form

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with modern design principles
- **Icons**: Unicode symbols and emojis for lightweight icons
- **Fonts**: Google Fonts (Inter)

## Quick Start

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:

   ```bash
   python run.py
   ```

   or

   ```bash
   python app.py
   ```

3. **Open Your Browser**:
   Navigate to `http://localhost:5000`

## Project Structure

```
flask_portfolio/
├── app.py                 # Main Flask application
├── run.py                 # Application runner script
├── requirements.txt       # Python dependencies
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Main portfolio page
│   └── 404.html          # Error page
└── static/
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── main.js       # JavaScript functionality
```

## Customization

### Updating Personal Information

Edit the `portfolio_data` dictionary in `app.py` to update:

- Personal details
- Work experience
- Skills and technologies
- Education information
- Projects

### Styling Changes

Modify `static/css/style.css` to customize:

- Colors and branding
- Layout and spacing
- Animations and effects
- Responsive breakpoints

### Adding New Sections

1. Update the data structure in `app.py`
2. Add the HTML section in `templates/index.html`
3. Add corresponding CSS styles
4. Update navigation links

## Contact Form

The contact form is fully functional and will:

- Validate all required fields
- Display success/error messages
- Log submissions to the console (can be extended to email/database)

## Deployment Options

### Local Development

```bash
python run.py
```

### Production Deployment

- **Heroku**: Ready for Heroku deployment
- **Vercel**: Compatible with Vercel
- **DigitalOcean**: Deploy on any VPS
- **AWS/GCP**: Cloud deployment ready

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Performance Features

- Optimized CSS and JavaScript
- Efficient animations
- Compressed assets
- Fast loading times
- Mobile-optimized

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions about this portfolio:

- **Email**: kashishchopra2k05@gmail.com
- **GitHub**: github.com/kashishchopra
- **Location**: Dwarka, New Delhi

---

