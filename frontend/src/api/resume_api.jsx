import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const optimizeResume = async (file, jobDescription) => {

    const formData = new FormData();

    formData.append("file", file);
    formData.append("job_description", jobDescription);

    const response = await API.post(
        "/optimize-resume",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};