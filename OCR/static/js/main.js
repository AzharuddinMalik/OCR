document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenu = document.querySelector('.mobile-menu');
    const navLinks = document.querySelector('.nav-links');

    mobileMenu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            // Check if the link is an anchor within the same page
            const targetId = this.getAttribute('href');
            if (targetId.startsWith('#') && document.querySelector(targetId)) {
                document.querySelector(targetId).scrollIntoView({
                    behavior: 'smooth'
                });
            } else {
                // If it's a regular link, navigate
                window.location.href = targetId;
            }
        });
    });

    // Animation on scroll
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.feature-card').forEach(card => {
        card.classList.add('animate-fade-in');
        observer.observe(card);
    });
});



//==================== Dark Mode Toggle //====================
const themeToggle = document.querySelector('.theme-toggle');
const themeIcon = document.getElementById('themeIcon');
const body = document.body;

//==================== Load saved theme //====================
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    body.setAttribute('data-theme', savedTheme);
    themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
}

themeToggle.addEventListener('click', () => {
    if (body.getAttribute('data-theme') === 'dark') {
        body.removeAttribute('data-theme');
        themeIcon.className = 'fas fa-moon';
        localStorage.setItem('theme', 'light');
    } else {
        body.setAttribute('data-theme', 'dark');
        themeIcon.className = 'fas fa-sun';
        localStorage.setItem('theme', 'dark');
    }
});

//==================== File Upload Handling //====================
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const analyzeBtn = document.getElementById('analyzeBtn');

//==================== Drag & drop handlers //====================
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length) handleFile(files[0]);
    // The preview logic was a bit off, removed it for now as it's not directly used for image display on index.html
});

//==================== File input handler //====================
fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) handleFile(e.target.files[0]);
});

//==================== Analyze button handler //====================
analyzeBtn.addEventListener('click', async () => {
        if (!selectedFile) { // Use selectedFile instead of fileInput.files.length
            alert('Please select a file first!');
            return;
        }

        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';

        const formData = new FormData();
        formData.append('file', selectedFile); // Use selectedFile here

        try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json(); // This attempts to parse JSON

        if (response.ok) { // Check if the HTTP status was 2xx (e.g., 200 OK)
            // Pass both text and image_filename to the result page
            window.location.href = `/result?text=${encodeURIComponent(result.text)}&image_filename=${encodeURIComponent(result.image_filename)}`;
        } else {
            // If response.ok is false, it means server returned a non-2xx status (e.g., 400, 500)
            // The 'result' object should contain the 'error' message from the backend.
            alert('Error: ' + (result.error || 'An unknown error occurred during analysis.'));
        }
    } catch (error) {
        console.error('Fetch or JSON parsing error:', error);
        alert('Analysis failed. Please try again. (Client-side error)');
    } finally {
        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML = '<i class="fas fa-magic"></i> Analyze Document';
    }
});

    // Ensure fileInput change also uses handleFile
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) handleFile(e.target.files[0]);
    });

let selectedFile = null; // A global variable to store the selected file

// Update handleFile function
function handleFile(file) {
    const validTypes = ['image/jpeg', 'image/png', 'application/pdf', 'image/gif', 'image/heic'];
    if (!validTypes.includes(file.type)) {
        alert('Please upload a valid file type (JPG, PNG, GIF, HEIC, PDF)');
        return;
    }

    selectedFile = file;

    const filePreview = document.getElementById('filePreview');
    filePreview.innerHTML = `
        <div class="file-info">
            <i class="fas fa-file-alt file-icon"></i>
            <div class="file-details">
                <div class="file-name">${file.name}</div>
                <div class="file-size">${(file.size / 1024).toFixed(1)} KB</div>
            </div>
        </div>
    `;
    filePreview.classList.add('active');
}

// Add clear functionality
document.getElementById('clearBtn').addEventListener('click', () => {
    selectedFile = null;
    fileInput.value = '';
    document.getElementById('filePreview').innerHTML = '';
    document.getElementById('filePreview').classList.remove('active');
});



//=============== Contact Form Handling //===============
const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const submitButton = this.querySelector('button');
    submitButton.innerHTML = 'Sending... <i class="fas fa-spinner fa-spin"></i>';

    const formData = new FormData(this);

    fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            alert('Message sent successfully!');
            this.reset();
        } else {
            alert('Oops! Something went wrong. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to send message. Please check your connection.');
    })
    .finally(() => {
        submitButton.innerHTML = 'Send Message <i class="fas fa-paper-plane"></i>';
    });
});
