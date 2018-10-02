import matplotlib.pyplot as plt

string = "Cluster 36 titles: Curricular Process and Communicative Conception in Physics Education (2008), How Abstract is Abstract? Signs, Salience, and Meaning in Physics (2008), Inside the Golden Kingdom: Views of Physics from 'Inside the Double Bind' (2008), Comparing Cluster Analysis and Traditional Analysis Methods in PER: More Data (2009), Broadening Our Lens: Socio-Cultural Perspectives in PER (Part I: Artifacts and Mediation) (2009), Broadening Our Lens: Socio-Cultural Perspectives in PER (Part II: Communities & Social Interaction) (2009), Adaptation and Implementation of the Physics and Everyday Thinking Curriculum in a High School Physics Classroom (2011), The Next Generation Science Standards: To What Extent are Modern Physics Concepts Included? (2012), The Research Subfield Choice of Women in Academic Physics: A Pilot Study (2012), Where do physics students come from and what do they become? A look at knowledge and identity pathways through and beyond school experience (2012), Interdisciplinary thinking and physics identity (2013), Rethinking the Locus of Evaluation to Promote Classroom Scientific Induction (2013), Fleeting but powerful: How affect matters for teaching, learning, and doing physics (2013), 3rd year university physics students  reasoning on physical information encoded in quantum state at a point in time (2014), Identifying and supporting children's narrative reasoning about physical phenomena (2014), Thinking in Physics -- a book about teaching (2014), Magnetism 2.0: Concept and Evaluation of a Multimedia Learning Environment (2014), Pathways to STEM: Understanding Identity of Adult Physicists through Narrative Analysis (2015), Physics Learning Facilitates Enhanced Resting-State Brain Connectivity in Problem-Solving Network (2015), Physics teacher production: Patterns of institutional engagement and faculty theories (2015), Technology and research-based strategies: an experience in Chile (2015), Thinking in Physics   the book and the website (2015), Research on student conceptions of integration in math and physics (2015), Analysing discourse and identity in physics education: Methodological considerations (2016), Epistemic Games and Activity Theory: A Multi-Layered Task Analysis (2016), Investigating Student Understanding of Vector Calculus in Junior-Level E&M (2016), On the Interaction of Physics with Physics Education Research (2016),"

print(2008,string.count("(2008)"))
print(2009,string.count("(2009)"))
print(2010,string.count("(2010)"))
print(2011,string.count("(2011)"))
print(2012,string.count("(2012)"))
print(2013,string.count("(2013)"))
print(2014,string.count("(2014)"))
print(2015,string.count("(2015)"))
print(2016,string.count("(2016)"))

print("There are {} documents in this cluster".format(string.count("(2008)")+string.count("(2009)")+string.count("(2010)")+string.count("(2011)")+string.count("(2012)")+string.count("(2013)")+string.count("(2014)")+string.count("(2015)")+string.count("(2016)")))

plt.plot([2008,2009,2010,2011,2012,2013,2014,2015,2016], [string.count("(2008)"),string.count("(2009)"),string.count("(2010)"),string.count("(2011)"),string.count("(2012)"),string.count("(2013)"),string.count("(2014)"),string.count("(2015)"),string.count("(2016)")], linewidth=2.0)
plt.axis([2007, 2018, 0, 10])
plt.show()