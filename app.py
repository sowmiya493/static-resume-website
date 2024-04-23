from flask import Flask, render_template, request, send_file
import boto3
import os
import tempfile

app = Flask(__name__)  # Assuming templates are in the 'templates' directory

# AWS S3 configuration
S3_BUCKET = 'resume-21ita49'
AWS_ACCESS_KEY_ID = 'AKIAVRUVRFQPNV7HCCMM'
AWS_SECRET_ACCESS_KEY = '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'

s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def format_resume(name, email, phone, address, linkedin, github,
                   education, softskills, technicalskills, interests,
                   certificates, projects, internship, languages):
    resume_text = f"{name} \n {email}\n{phone} | {address} | LinkedIn: {linkedin} | GitHub: {github}\n\n"
    resume_text += "Education: \n" + "\n".join(education.split(',')) + "\n\n"
    resume_text += "Certificates:\n" + "\n".join(certificates.split(',')) + "\n\n"
    resume_text += "Soft Skills:\n" + "\n".join(softskills.split(',')) + "\n\n"
    resume_text += "Technical Skills:\n" + "\n".join(technicalskills.split(',')) + "\n\n"
    resume_text += "Interests:\n" + "\n".join(interests.split(',')) + "\n\n"
    resume_text += "Languages Known:\n" + "\n".join(languages.split(',')) + "\n\n"
    resume_text += "Projects: \n" + "\n".join(projects.split(',')) + "\n\n"
    resume_text += f"Internship: {internship}\n"
    return resume_text

@app.route('/')
def index():
    return render_template('index.html', success_message="")

@app.route('/submit', methods=['POST'])
def submit_resume():
    if request.method == 'POST':
        # Retrieve form data using request.form.get() to handle missing keys
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        phone = request.form.get('phone', '')
        address = request.form.get('address', '')
        linkedin = request.form.get('linkedin', '')
        github = request.form.get('github', '')
        education = request.form.get('education', '')  
        softskills = request.form.get('softskills','')
        languages = request.form.get('languages','')
        technicalskills = request.form.get('technicalskills','')
        interests = request.form.get('interests','')
        certifications = request.form.get('certifications','')
        projects = request.form.get('projects','')
        internship = request.form.get('internship','')


        resume_text = format_resume(name, email, phone, address,
                                     linkedin, github, education, softskills,
                                     technicalskills, interests, certifications,
                                     projects, internship, languages)

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(resume_text)

        temp_file.close()  # Close the temporary file explicitly

        s3.upload_file(temp_file_path, S3_BUCKET, 'resume.txt')

        os.remove(temp_file_path)

        success_message = "Resume submitted successfully"
        return render_template('index.html', success_message=success_message)

@app.route('/download')
def download_resume():
    try:
        temp_file_path = tempfile.mktemp(suffix='.txt')
        s3.download_file(S3_BUCKET, 'resume.txt', temp_file_path)
        return send_file(temp_file_path, as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
