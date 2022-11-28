### Recreate 
Generate
```bash
mvn archetype:generate -DgroupId=com.datadoghq.gitmetadatapoc -DartifactId=gitmetadatapoc -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

Add plugin to the pom.xml
```xml
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-jar-plugin</artifactId>
        <version>3.1.0</version>
        <configuration>
          <archive>
           <manifest>
             <mainClass>com.datadoghq.gitmetadatapoc.App</mainClass>
           </manifest>
          </archive>
        </configuration>
      </plugin>
    </plugins>
  </build>
```

Build
```bash
mvn package
```

Download dd agent
```bash
wget -O dd-java-agent.jar https://dtdg.co/latest-java-tracer
```

Run
```bash
java -javaagent:../../dd-java-agent.jar -Ddd.service=my-app -Ddd.env=staging -Ddd.version=1.0 -jar target/gitmetadatapoc-1.0-SNAPSHOT.jar
```
