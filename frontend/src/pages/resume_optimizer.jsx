import { useState } from "react";
import { optimizeResume } from "../api/resume_api";

export default function ResumeOptimizer() {
    const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleOptimize = async () => {
    try {
      setLoading(true);

      const data = await optimizeResume(
        file,
        jobDescription
      );
      console.log("Backend response:");
      console.log(data);

      setResult(data);
    } catch (err) {
      console.error(err);
      alert("Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "1000px",
        margin: "40px auto",
        fontFamily: "Arial",
      }}
    >
      <h1>AI Resume Copilot</h1>

      <input
        type="file"
        accept=".pdf,.doc,.docx"
        onChange={(e) => setFile(e.target.files[0])}
        />

      <textarea
        rows={8}
        placeholder="Paste Job Description"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        style={{ width: "100%", marginBottom: 20 }}
      />

    <button
        onClick={handleOptimize}
        disabled={loading}
        style={{
        marginTop: "20px",
        padding: "12px 24px",
        fontSize: "16px",
        cursor: "pointer",}}>
    {loading ? "Optimizing..." : "Optimize Resume"}
    </button>

      {result && (
        <div style={{ marginTop: 40 }}>

          <hr />

          <h2>ATS Score</h2>

          <h3>
            {result.ats_score_before} → {result.ats_score_after}
          </h3>

          <hr />

          <h2>Section Scores</h2>

          <table border="1" cellPadding="8">
            <tbody>
              {Object.entries(result.section_scores || {}).map(([key, value]) => (
                <tr key={key}>
                  <td>{key}</td>
                  <td>{value}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <hr />

          <h2>Keywords Added</h2>

          <ul>
            {result.keywords_added?.map((k) => (
              <li key={k}>{k}</li>
            ))}
          </ul>

          <hr />

          <h2>Missing Keywords</h2>

          <ul>
            {result.keywords_missing?.map((k) => (
              <li key={k}>{k}</li>
            ))}
          </ul>

          <hr />

          <h2>Strongest Section</h2>

          <p>{result.strongest_section}</p>

          <h2>Weakest Section</h2>

          <p>{result.weakest_section}</p>

          <hr />

          <h2>Recruiter Decision</h2>

          <p>
            <b>Decision:</b>{" "}
            {result.recruiter_decision?.decision}
          </p>

          <p>
            <b>Hire Probability:</b>{" "}
            {result.recruiter_decision?.hire_probability}
          </p>

          <p>
            <b>Confidence:</b>{" "}
            {result.recruiter_decision?.confidence}
          </p>

          <p>
            <b>Comment:</b>{" "}
            {result.recruiter_decision?.comment}
          </p>

          <hr />

          <h2>Recommendations</h2>

          <h3>Must Fix</h3>

          <ul>
            {result.recommendations?.must_fix?.map((r, i) => (
              <li key={i}>{r}</li>
            ))}
          </ul>

          <h3>Nice To Have</h3>

          <ul>
            {result.recommendations?.nice_to_have?.map((r, i) => (
              <li key={i}>{r}</li>
            ))}
          </ul>

          <hr />

          <h2>Recruiter Questions</h2>

          <ol>
          {result.interview_questions?.map((q, i) => (
              <li key={i}>
                <b>{q.question}</b>

                <br />

                <small>{q.reason}</small>
              </li>
            ))}
          </ol>

          <hr />

          <h2>Improved Bullets</h2>

          {result.improved_bullets?.map((b, i) => (
            <div
              key={i}
              style={{
                border: "1px solid #ddd",
                padding: 15,
                marginBottom: 15,
              }}
            >
              <p>
                <b>Section:</b> {b.section}
              </p>

              <p>
                <b>Original:</b>
              </p>

              <p>{b.original}</p>

              <p>
                <b>Improved:</b>
              </p>

              <p>{b.improved}</p>

              <p>
                <b>Reason:</b> {b.reason}
              </p>
            </div>
          ))}

          <hr />

          <h2>Final Recruiter Feedback</h2>

          <p>{result.final_recruiter_feedback}</p>

        </div>
      )}
    </div>
  );
}