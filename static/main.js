const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file');
const originalDropZoneHTML = dropZone.innerHTML;

// Function to handle file upload
const handleFileUpload = (file) => {
    // Update UI state
    dropZone.innerHTML = 'Upload successful, processing the file...';
    dropZone.classList.add('uploading');

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;
        } else if (data.error) {
            throw new Error(data.error);
        }
    })
    .catch(error => {
        // Restore original state
        dropZone.innerHTML = originalDropZoneHTML;
        dropZone.classList.remove('uploading');
        alert('Upload failed: ' + error.message);
    });
};

// Click on drop zone to upload
dropZone.addEventListener('click', () => {
    if (!dropZone.classList.contains('uploading')) {
        fileInput.click();
    }
});

// File selection
fileInput.addEventListener('change', function(e) {
    if (this.files.length) {
        const file = this.files[0];
        if (!file.name.endsWith('.py')) {
            alert('Only Python (.py) files are allowed.');
            return;
        }
        handleFileUpload(file);
    }
});

// Drag and drop handlers
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    if (!dropZone.classList.contains('uploading')) {
        dropZone.classList.add('dragover');
    }
});

dropZone.addEventListener('dragleave', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');

    if (dropZone.classList.contains('uploading')) return;

    const files = e.dataTransfer.files;
    if (!files.length) return;

    const file = files[0];
    if (!file.name.endsWith('.py')) {
        alert('Only Python (.py) files are allowed.');
        return;
    }

    handleFileUpload(file);
});