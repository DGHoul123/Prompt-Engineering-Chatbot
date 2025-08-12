# Zero-shot vs. Few-shot Prompting for Text Summarization

This project compares the effectiveness of zero-shot and few-shot prompting techniques for the task of text summarization. The objective is to analyze how providing the LLM with examples impacts the quality and accuracy of the generated summary.

## Zero-shot Prompting

### Prompt
```
Summarize the following article in two paragraphs. Make sure to capture the main points and key arguments.
Just a random article by Alphabyte
```
### Output

The article explores the concept that while randomness appears to dominate many aspects of life—from dice rolls and sunflower seed patterns to the arrangement of stars—it often leads to predictable patterns over time. Using the example of the Galton Board, where beads randomly fall left or right but consistently form a bell curve, it illustrates how order can emerge from seemingly random events. The predictable distribution occurs because certain outcomes (like beads falling into central bins) are statistically more likely than others, showing that probability can shape randomness into structured results.

Extending this idea to human behavior, the article argues that social group formation works in a similar way. In new environments, initial connections may be random, but over time, people naturally gravitate toward others with shared traits, values, or interests, while drifting away from incompatible groups. This “order from randomness” suggests that forcing yourself to fit into groups where you don’t naturally belong rarely works—authentic compatibility determines lasting bonds. The conclusion is that by allowing time and natural tendencies to work, you’ll eventually find yourself surrounded by people with whom you genuinely connect.

## Few-shot Prompting

### Prompt
```
Topic: Bidirectional associations between sleep (quality and duration) and psychosocial functioning across the university years.
Summary: Tavernier and Willoughby’s (2014) study explored the relationships between university students’ sleep and their
intrapersonal, interpersonal, and educational development. While the authors cited many scholars who have explored these
relationships, they pointed out that most of these studies focused on unidirectional correlations over a short period of time.
In contrast, Tavernier and Willoughby tested whether there was a bidirectional or unidirectional association between participants’
sleep quality and duration and several psychosocial factors including intrapersonal adjustment, friendship quality, and academic
achievement.Further they conducted a longitudinal study over a period of three years in order to determine whether there were
changes in the strength or direction of these associations over time. They predicted that sleep quality would correlate with
measures of intrapersonal adjustment, friendship quality, and academic achievement; they further hypothesized that this
correlation would be bidirectional: sleep quality would predict psychosocial measures and at the same time, psychosocial measures
would predict sleep quality.



Topic: The Importance Of Time Management For Students
Summary: Michael Adams’ article, “The Importance of Time Management for Students,” published on April 12, 2024, underscores the
vital role of time management in achieving academic success and reducing stress. The article begins by outlining the typical time
management challenges students face, including the difficulty of balancing academic responsibilities with extracurricular activities
and personal life.

In the article’s body, Adams provides actionable strategies for effective time management. He offers practical advice on prioritizing
tasks, setting clear and realistic goals, and combating procrastination. These strategies are illustrated with real-life examples to
demonstrate how students can apply them to enhance their productivity and academic performance. The article concludes by emphasizing
the importance of developing robust time management skills to harmoniously balance academic obligations and personal well-being.
Adams advocates for students to adopt these skills to improve their academic outcomes and achieve a more manageable and less stressful
lifestyle.

Overall, this article is crucial for students aiming to boost their productivity and academic success through improved time management.
It provides valuable insights and practical tips to help students navigate their responsibilities more effectively.


Now, summarize the following article in a similar style and format:
Article: Just a random article by Alphabyte 
Summary:
```

### Output
Topic: Just a Random Article

Summary: Alphabyte’s article, *Just a Random Article*, reflects on how randomness appears throughout life yet often gives rise to predictable patterns and natural order. Using everyday examples such as dice rolls, sunflower seed arrangements, and the positioning of stars, the author illustrates the omnipresence of randomness. This idea is further explored through the Galton Board experiment, where beads fall randomly left or right but consistently form a bell curve, demonstrating how probability shapes seemingly chaotic events into structured outcomes.

The article extends this concept to human social dynamics, noting that when entering new environments—such as a school, college, or workplace—initial social connections may be random. Over time, however, individuals tend to gravitate toward those with similar traits, values, or interests, while drifting away from incompatible groups. Drawing on Mark Manson’s ideas from *The Subtle Art of Not Giving a F\*\*k*, Alphabyte emphasizes that authentic compatibility, rather than forced adaptation, leads to lasting connections. The overarching message is to allow time and natural tendencies to guide you toward people and situations where you truly belong.

## Analysis & Conclusion

The few-shot style summary was clearly the stronger output, as it not only conveyed the main points of Alphabyte’s article but also followed the exact “Topic” and “Summary” structure you had demonstrated earlier. Compared to the zero-shot attempt, it was more organized, matched the tone of your examples, and balanced brevity with detail, ensuring that both the overarching idea and the supporting insights were captured. The main difference lay in structure and precision—the zero-shot version flowed as a natural paragraph but lacked the formal labeling and consistent format, while the few-shot version mirrored your examples closely, offering a more professional and reusable format. The examples served as a concrete template, eliminating ambiguity about length, tone, and scope, which meant the model could focus entirely on content rather than guessing at presentation. This experiment shows how powerful prompt engineering can be: by providing explicit examples, you essentially “train” the model in real time to replicate the desired structure and style, turning a good but generic response into one that is precise, polished, and perfectly aligned with your needs.
