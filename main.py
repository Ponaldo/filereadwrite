import sys


def main():
    print("Reading the file:")
    try:
        freader = open("C:/Users/neetu/OneDrive/Documents/AI to the moon/Artifical_intelligence_ideas.txt", "r")
        print(freader.read())
        freader.close()
        try:
            lreader = open("C:/Users/neetu/OneDrive/Documents/AI to the moon/Artifical_intelligence_ideas.txt", "a")
            lreader.write("pooplypotty")
            lreader.close()
            try:
                zreader = open("C:/Users/neetu/OneDrive/Documents/AI to the moon/Artifical_intelligence_ideas.txt", "r")
                print("Here is the new version of the file")
                print(zreader.read())
                zreader.close()
            except FileNotFoundError:
                print("big error this file not exist")
        except FileNotFoundError:
            print("big error this file not exist")

    except ValueError:
        print("big error this file 76")
    except:
        print("big error this file 78")
    finally:
        print("execute")


main()
