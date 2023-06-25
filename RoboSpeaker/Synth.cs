
        using System;
        using System.Speech.Synthesis;

        public class Synth
        {
            public static void Main()
            {
                using (SpeechSynthesizer synth = new SpeechSynthesizer())
                {
                    synth.Speak("Hi");
                }
            }
        }
        