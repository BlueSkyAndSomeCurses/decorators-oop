package ua.edu.ucu.apps.decorator;

public interface AbstractDecorator {
  SmartDocument wrappee = null;

  String parse();
}
