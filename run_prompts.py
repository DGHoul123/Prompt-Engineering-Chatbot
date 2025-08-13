import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))


model = genai.GenerativeModel('gemma-3n-e2b-it')


few_shot_prompt = """
Topic: Bidirectional associations between sleep (quality and duration) and psychosocial functioning across the university years.
Summary: Tavernier and Willoughby’s (2014) study explored the relationships between university students’ sleep and their intrapersonal, interpersonal, and educational development. While the authors cited many scholars who have explored these relationships, they pointed out that most of these studies focused on unidirectional correlations over a short period of time. In contrast, Tavernier and Willoughby tested whether there was a bidirectional or unidirectional association between participants’ sleep quality and duration and several psychosocial factors including intrapersonal adjustment, friendship quality, and academic achievement. Further they conducted a longitudinal study over a period of three years in order to determine whether there were changes in the strength or direction of these associations over time. They predicted that sleep quality would correlate with measures of intrapersonal adjustment, friendship quality, and academic achievement; they further hypothesized that this correlation would be bidirectional: sleep quality would predict psychosocial measures and at the same time, psychosocial measures would predict sleep quality.



Topic: The Importance Of Time Management For Students
Summary: Michael Adams’ article, “The Importance of Time Management for Students,” published on April 12, 2024, underscores the vital role of time management in achieving academic success and reducing stress. The article begins by outlining the typical time management challenges students face, including the difficulty of balancing academic responsibilities with extracurricular activities and personal life.
In the article’s body, Adams provides actionable strategies for effective time management. He offers practical advice on prioritizing tasks, setting clear and realistic goals, and combating procrastination. These strategies are illustrated with real-life examples to demonstrate how students can apply them to enhance their productivity and academic performance.
The article concludes by emphasizing the importance of developing robust time management skills to harmoniously balance academic obligations and personal well-being. Adams advocates for students to adopt these skills to improve their academic outcomes and achieve a more manageable and less stressful lifestyle.
Overall, this article is crucial for students aiming to boost their productivity and academic success through improved time management. It provides valuable insights and practical tips to help students navigate their responsibilities more effectively.


Now, summarize the following article in a similar style and format:
Article: Just a random article by Alphabyte
Summary:
"""

response = model.generate_content(few_shot_prompt)

print("Few-shot Prompt Summary:")
print(response.text)

