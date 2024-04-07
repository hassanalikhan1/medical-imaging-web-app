// components/UploadDICOM.js
import React, { useState } from 'react';
import axios from 'axios';

const UploadDICOM = () => {
    const [file, setFile] = useState(null);

    const onFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const onUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:8000/api/upload-dicom/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log(response.data);
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div>
            <h2>Upload DICOM Images</h2>
            <input type="file" accept=".dcm" onChange={onFileChange} />
            <button onClick={onUpload}>Upload</button>
        </div>
    );
};

export default UploadDICOM;
