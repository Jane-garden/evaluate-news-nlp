# evaluate-news-nlp

proje1-Legal Reading Comprehension

Project Overview

This project focused on building machine reading comprehension models for judicial documents. Court rulings contain rich information such as time, location, and relationships among parties. By enabling intelligent understanding of these documents, we can support judges, lawyers, and the public in retrieving case information more efficiently.

The task covered multiple document types (civil, criminal, administrative) and required multi-hop reasoning — answers could not be derived from a single sentence but needed reasoning across multiple sentences.

Dataset
	•	~5,100 question-answer pairs (≈1,700 each for civil, criminal, and administrative cases).
	•	Data split: 90% training, 10% testing.
	•	Format aligned with HotpotQA, including context, question, answer, and supporting facts.
	•	Answer types included text spans, yes/no, and unanswerable (“unknown”).

My Contribution
	•	Implemented baseline models and trained them on the dataset.
	•	Conducted evaluation on the development set using standard QA metrics (exact match and F1).
	•	Explored improvements with additional legal datasets (e.g., CJRC) and experimented with pretrained models such as LegalBERT and Judicial BERT.
	•	Investigated advanced architectures like graph neural networks (GNNs) to enhance multi-hop reasoning.

Outputs
	•	Successfully reproduced baseline results and improved performance by incorporating domain-specific pretrained models.
	•	Demonstrated measurable gains in multi-hop reasoning accuracy on legal texts.
	•	Delivered a structured report analyzing model design, experimental results, and potential applications in legal AI.

⸻

要不要我再帮你整理成 简历 bullet points 的版本（比如适合放在“Projects”里，3–4条精炼的点）？
