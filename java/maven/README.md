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

Run
```bash
java -jar target/gitmetadatapoc-1.0-SNAPSHOT.jar
```
