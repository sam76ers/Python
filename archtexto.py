import pandas as pd
df = pd.read_csv(r'C:\Users\sam76\Documents\Python\CSV\datos_medicinaV2.csv', sep = ';')
print(df.shape)
#print(df.iloc[5,7])
#x = df[['id_estudiante']]
#print(df.describe())

#Obtener Archivo sin nulos
df_sin_null=df.copy()
df_sin_null=df_sin_null.dropna()
#print(df_sin_null['gestion'].value_counts())
#Definición de parámetros
nivel_curso=1
gestion_curso=2019
materia='FARMACOLOGIA'
#print(df[df.nivel==nivel_curso,df.gestion==gestion_curso])
#Obtener los cursantes de un nivel y de una gestión
df1=df_sin_null.loc[(df['nivel']==nivel_curso)&(df['gestion']==gestion_curso)&(df['materia']==materia)]
#Obtener los cursantes de un nivel y de una gestión anterior
df2=df_sin_null.loc[(df['nivel']==nivel_curso)&(df['gestion']==gestion_curso-1)&(df['materia']==materia)]

#Llevar a conjuntos los dataframes generados
cursantes=set(df1['id_estudiante'])
cursantes_anterior=set(df2['id_estudiante'])
#Intersección de conjuntos
repitentes=cursantes.intersection(cursantes_anterior)
print(len(repitentes))
#df2=df1.loc[df['gestion']==gestion_curso]
#print(df.gestion())
#print(df2.info())


