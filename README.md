# research-paper-classification

My idea of legwork for a AI research assistant in parts of Quantitative Biology as catgorized in [arxiv.org](https://arxiv.org/category_taxonomy).
Legwork in terms of finding splitting strategy on the pdf files pain in the a.., and while at it brainstorm on the graph model (nodes relationships and etc etc etc) that will play as the second brain to semantic vector search (does that mean that's the first brain?).

### notes;

using arxiv.org's and thinking on results that will fetch `cat:bioT` papers we can do something along the lines of

```python
anatomical_structures = {
    "heart": "organ",
    "liver": "organ",
    "kidney": "organ",
    "cardiac muscle": "tissue",
    "epithelial": "tissue",
    "connective": "tissue",
    "muscle tissue": "tissue",
    "nervous tissue": "tissue",
}
```

**It's not all organs and tissues**

First attempt does not make sense for this my use case, need to broaden the classification strategy:

Looking at these papersand rethinking the classification strategy beyond just tissues and organs. Based on their contents, I think the following key classification dimensions could-just-might-be more meaningful:

1. **Methodological Approach**:

- Biophysical/Mathematical Modeling (like bell's model for adhesion)
- Experimental Studies
- Image Analysis and Microscopy
- Computational Simulations

`for future self`

What is it and why in Odin's name i'm using this?

`this represents the scientific methods/approaches used`

Very valuable for researchers wanting to:

`Find papers using similar methods to replicate studies` who cheated

`Discover new methods for their research` how to cheat

`Compare different methodological approaches for the same problem`  who is cheating with me

2. \*Scale of Investigation\*\*: can I please think of another name?? reminds me of my theology school days

- Molecular Level ( protein interactions, binding kinetics)
- Cellular Level (cell mechanics, adhesion)
- Tissue Level
- Organ Level

`note to the self`

`represents the level at which the research was conducted` that's why all the repeated `level`s

`one way to help with providing a targetted response`, for example when a user asks/prompts: 

`Ah, rememeber the day we were talking about Cell adhesion at your wedding? we never got to finish it`

3. **Core Focus Area**:
- Mechanobiology
- Cell-cell Interactions
- Tissue Mechanics
- Disease Mechanisms
- Biomaterial Development
- Systems biology

`note to self` 

Like Scale told us at **what level**, this one is for telling us about `about what`, mira

Scale: Cellular level
Focus Areas: Cell-Cell Interactions

Thinking that this be useful for research assistant to understand both the level and subject of interest



4. **Technical Aspects**:
- Force Measurements
- Microscopy and Imaging
- Computational Methods
- Material Characterization
- Statistical Analysis

`note to self`

represents the tools, techniques,and analytical methods used

Thought was that it is would be useful for a research assistant because:
- Helpful in order to identify methodological overlaps between different fields
- Allows researcher to find papers using certain specific technique(s)
- ?maybe? helps for understanding/validating experimental designs

5. **Application Context**:
- Basic Research
- Clinical Applications
- Therapeutic Development
- Diagnostic Tools

`note to the self`

helps research assistant connect theoretical work to practical applications

This dimension helps bridge the gap between "what did we learned" and "how we can use it" and should be valuable for both researchers and practitioners in the field. I sure do hope so.

This multi dimensional classification would be more useful because?:

1. more-better (new word) reflects how researchers actually approach and use these papers
2. It makes it easier to identify related methodologies across different biological systems
3. Helps identify potential collaborations or cross-pollination :) of techniques



### Graph Model


```cypher
// Core elements we identified:
1. Paper (node)
2. Method (nodes: Biophysical Modeling, Experimental Studies, etc.)
3. Scale (nodes: Molecular, Cellular, Tissue)
4. Focus (nodes: Mechanobiology, Tissue Mechanics, etc.)
5. TechnicalAspect (nodes: Force Measurements, etc.)
6. Application (nodes: Basic Research, Wound Healing, etc.)
```

For semantic search, the embeddings could reside in:

The Paper node properties where we store:

```
Abstract embedding
Full text embedding
Title embedding
```

This way when a user searches,, we compare their query embedding against these different text components


Each categorical node (Method, Scale, Focus etc etc) could also have embeddings of their **descriptions/definitions**, allowing users to find relevant categories even if they use different terminology


**rough outline of the ingestion process and cyphers to populate the graph**

for each paper we extract and vectorize its

- Abstract embedding
- Full text embedding
- Title embedding

then generate the Cypher queries for creating the (p:Paper) adding the embeddings of abstract, fulltext, title then various dimension nodes with their own embedings (?storage space!!!) and relationships - see cyphers above

move to the next research paper, this is depicted by Cypher queries below:

---

```cypher
// First create the Paper node with its embeddings
CREATE (p:Paper {
    title: "Interplay of damage and repair in the control of epithelial tissue integrity in response to cyclic loading",
    authors: ["Eleni Papafilippou", "Lucia Baldauf", "Guillaume Charras", "Alexandre J. Kabla", "Aessandra Bonfanti"],
    year: 2024,
    title_embedding: [...],      // Vector here
    abstract_embedding: [...],   // Vector here
    fulltext_embedding: [...]    // and Vector here
})

// the dimensionalities, Smokey

//Create Method nodes and relationships
MERGE (m1:Method {
    name: "Biophysical Modeling",
    description: "Mathematical and physical models applied to biological systems",
    description_embedding: [...]  // Vector here
})
MERGE (m2:Method {
    name: "Experimental Studies",
    description: "Research conducted through direct manipulation and observation",
    description_embedding: [...]  // Vector here
})
CREATE (p)-[:USES_METHOD]->(m1)
CREATE (p)-[:USES_METHOD]->(m2)

// Create Scale nodes and relationships
MERGE (s1:Scale {
    name: "Molecular",
    description: "Investigation at the level of individual molecules and their interactions",
    description_embedding: [...]  // Vector here
})
MERGE (s2:Scale {
    name: "Cellular",
    description: "Studies focused on cell-level processes and behaviors",
    description_embedding: [...]  //vector here
})
MERGE (s3:Scale {
    name: "Tissue",
    description: "Analysis of collective cell behavior and tissue-level properties",
    description_embedding: [...]  // Vector here
})
CREATE (p)-[:INVESTIGATES_AT_SCALE]->(s1)
CREATE (p)-[:INVESTIGATES_AT_SCALE]->(s2)
CREATE (p)-[:INVESTIGATES_AT_SCALE]->(s3)

// Create Focus nodes and relationships
MERGE (f1:Focus {
    name: "Mechanobiology",
    description: "Study of how physical forces influence biological systems",
    description_embedding: [...]  // Vector here
})
MERGE (f2:Focus {
    name: "Tissue Mechanics",
    description: "Study of mechanical properties and behavior of biological tissues",
    description_embedding: [...]  // Vector here
})
CREATE (p)-[:HAS_FOCUS]->(f1)
CREATE (p)-[:HAS_FOCUS]->(f2)

// Create TechnicalAspect nodes and relationships
MERGE (t1:TechnicalAspect {
    name: "Force Measurements",
    description: "Techniques for quantifying mechanical forces in biological systems",
    description_embedding: [...]  // Vector here
})
MERGE (t2:TechnicalAspect {
    name: "Mechanical Characterization",
    description: "Methods to analyze mechanical properties of biological materials",
    description_embedding: [...]  // Vector here
})
CREATE (p)-[:INVOLVES_TECHNIQUE]->(t1)
CREATE (p)-[:INVOLVES_TECHNIQUE]->(t2)

// Create Application nodes and relationships
MERGE (a1:Application {
    name: "Basic Research",
    description: "Fundamental scientific investigation to advance understanding",
    description_embedding: [...]  // Vector here
})
MERGE (a2:Application {
    name: "Tissue Engineering",
    description: "Development of biological substitutes to restore tissue function",
    description_embedding: [...]  // Vector here
})
CREATE (p)-[:HAS_APPLICATION]->(a1)
CREATE (p)-[:HAS_APPLICATION]->(a2)
```

---

test this all out...