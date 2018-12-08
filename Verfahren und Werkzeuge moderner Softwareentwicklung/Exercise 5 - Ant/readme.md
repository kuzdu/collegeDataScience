# Ant

## Ant Script 
Ein eher unspektakuläres Ant Script, welches im Endeffekt nur ein HelloWorld.java ausführt. 

![Ant](images/ant.jpg "Ant")

Der dazugehörige Quellcode. 
```xml
<?xml version="1.0" encoding="UTF-8"?>

<project name="AntProject" default="main" basedir=".">
<description>
Description of your project
</description>

<property name="projectName" value="antproject" />  

<!--Staging Directory --> 
<property name="staging.dir" location="staging" />

<!-- Java sources -->
<property name="src.dir" location="src" />

<!-- Java classes -->
<property name="build.dir" location="${staging.dir}/bin" />

<!-- Output, Jar -->
<property name="dist.dir" location="${staging.dir}/dist" />

<target name="main" depends="clean, compile, dist" />

<target name="init">
<mkdir dir="${staging.dir}" />
<mkdir dir="${build.dir}" />
</target>

<target name="clean" description="Flush staging directory">
<delete dir="${staging.dir}" />   
</target>

<target name="compile" depends="init" description="compile the source ">
<javac includeantruntime="false" srcdir="${src.dir}" destdir="${build.dir}" />
</target>


<target name="dist" depends="compile" description="package, output to JAR">

<mkdir dir="${dist.dir}" />

<jar jarfile="${dist.dir}/${projectName}.jar" basedir="${build.dir}" >
<manifest>
<attribute name="Main-Class" value="${projectName}/AntProject" />
</manifest>
</jar>
</target>

</project>
```

