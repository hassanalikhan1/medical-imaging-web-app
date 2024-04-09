// components/UploadDICOM.js
import React, { useState, useEffect } from 'react';
import cornerstone from 'cornerstone-core';
import axios from 'axios';

/**
 * ${1:Description placeholder}
 * @date 4/9/2024 - 6:44:59 AM
 *
 * @returns {*}
 */
const UploadDICOM = () => {
    const [file, setFile] = useState(null);

    const onFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const onUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);
    
        try {
            const host = process.env.REACT_APP_BACKEND_HOST || 'http://localhost:5001';
            const response = await axios.post(`${host}/api/upload-dicom/`, formData, {
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


const DICOMViewer = ({ imageSrc }) => {
  useEffect(() => {
    // Initialize Cornerstone.js when the component mounts
    cornerstone.enable(document.getElementById('dicomContainer'));
    cornerstone.loadImage(imageSrc).then(image => {
      const element = document.getElementById('dicomContainer');
      cornerstone.displayImage(element, image);
    });
    return () => {
      // Cleanup when the component unmounts
      cornerstone.disable(document.getElementById('dicomContainer'));
    };
  }, [imageSrc]);

  return <div id="dicomContainer" style={{ width: '100%', height: '500px' }} />;
};

// export {} DICOMViewer;


export default UploadDICOM;
