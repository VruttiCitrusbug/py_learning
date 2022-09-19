import random
lst=['Acquiesce', 'Acronym', 'Ambiguity', 'Analogy', 'Anachronism', 'Antithesis', 'Antonym', 'Assonance', 'Brainstorming', 
  'Circumspect', 'Divergent', 'Eloquence', 'Emergent', 'Empathy', 'Enigma', 'Epitome', 'Epiphany', 'Erudite', 'Existential',
  'Exponential', 'Holistic', 'Homonym', 'Hubris', 'Hyperbole', 'Intellectual', 'Interactive', 'Irony',
  'Jargon', 'Juxtaposition', 'Malapropism', 'Magnanimous', 'Mentor', 'Metaphor', 'Monologue', 'Motif', 
  'Myriad', 'Nemesis', 'Nominal', 'Norms', 'Obfuscate','Paradox', 'Paraphrase', 'Pedantic', 'Pedagogy', 'Perusal', 'Phonemes', 
  'Phonological', 'Plagiarism', 'Plethora', 'Pretentious', 'Pseudonym', 'References', 'Reflection', 
  'Rubric', 'Sardonic', 'satire', 'Simile', 'Syntax', 'Thesis', 'Validity', 'Vernacular', 'Virtual', 
  'Vocational']
lstrw=list()
x=list()
c=0
fixpat=['|-----|','|','|','|','|','|','|','|','|','|','___']
fr=list()
rc=0
for i in range(10):
    lstrw.append(lst[random.randint(0, len(lst)-1)])
for ele in lstrw:
  fr.clear()
  rc=0
  for i in range(10):
      x.clear()
      c=0
      tstele=ele
      for j in range(2):
        x.append(random.randint(0,len(ele)-1))
      x=[*set(x)]
      for e in x:  
        tstele=tstele.replace(ele[e],'_')
      print(tstele)
      inp=input("enter answer")
      if len(inp)==len(ele):
        for e in x:
          if inp[e]==ele[e]:
            c+=1
      if c==len(x):
          if rc==0:
              for t in fixpat:
                print(t)
              break
          else:
            for r in fr:
                    print(r)
            for m in range(rc,len(fixpat)):
                    print(fixpat[m])
            break
      else:
        if i<5:
                    rc+=1
                    fr.append('{}  {}'.format('|','|'))
        elif i==5:
                    rc+=1
                    fr.append('{}  {}'.format('|','0'))
        elif i==6:
                    rc+=1
                    fr.append('{}  {}'.format('|','-'))
        elif i==7:
                    rc+=1
                    fr.pop()
                    fr.append('{}  {}{}'.format('|','-','|'))
        elif i==8:
                    rc+=1
                    fr.pop()
                    fr.append('{}  {}{}{}'.format('|','-','|','-'))
        elif i==9:
                    rc+=1
                    fr.append('{}   {}'.format('|','/\\'))
        for r in fr:
                      print(r)
        for m in range(rc,len(fixpat)):
                      print(fixpat[m])