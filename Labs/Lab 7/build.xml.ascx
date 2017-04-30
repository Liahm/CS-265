<project>

    <target name="clean">
        <delete dir="build">
    </target>

    <target name="compile">
        <mkdir dir="build/classes"/>
        <javac includeantruntime="false" srcdir="." destdir="build/classes"/>
    </target>

    <target name="jar">
            <mkdir dir="build/jar"/>
        <jar destfile="build/jar/prob1.jar" basedir="build/classes">
            <manifest>
                <attribute name="Main-Class" value="prob1"/>
            </manifest>
        </jar>
        <jar destfile="build/jar/prob2.jar" basedir="build/classes">
            <manifest>
                <attribute name="Main-Class" value="prob2"/>
            </manifest>
        </jar>  
        <jar destfile="build/jar/prob3.jar" basedir="build/classes">
            <manifest>
                <attribute name="Main-Class" value="prob3"/>
            </manifest>
        </jar>
        <jar destfile="build/jar/prob4.jar" basedir="build/classes">
            <manifest>
                <attribute name="Main-Class" value="prob4"/>
            </manifest>
        </jar>
    </target>

    <target name="prob1">
        <java jar="build/jar/prob1.jar" fork="true">
            <arg value="Potato"/>
            </java>
    </target>
    <target name="prob2">
        <java jar="build/jar/prob2.jar" fork="true">
            <arg value="74"/>
            </java>    
    </target>
    <target name="prob3">
        <java jar="build/jar/prob3.jar" fork="true">
            <arg value="2016"/>
            </java>    
    </target>
    <target name="prob4">
        <java jar="build/jar/prob4.jar" fork="true">
            <arg value="1"/>
            </java>    
    </target>            
</project>
