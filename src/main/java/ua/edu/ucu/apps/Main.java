package ua.edu.ucu.apps;

import ua.edu.ucu.apps.decorator.CacheDocument;
import ua.edu.ucu.apps.decorator.SmartDocument;
import ua.edu.ucu.apps.decorator.TimedDocument;

public class Main {
  public static void main(String[] args) {
    SmartDocument sd = new SmartDocument("/home/vitya/Downloads/1ceaf9c03d30fa7448693943986b35b0.jpg");

    TimedDocument td = new TimedDocument(sd);
    System.out.println(td.parse());

    CacheDocument cd = new CacheDocument(sd);
    cd.parse();
    cd.parse();
  }
}