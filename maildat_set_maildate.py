import time
import os
import shutil


def change_jobname():
    pass


def set_maildate():
    # process_dir = os.path.join(os.curdir, 'process')
    process_dir = os.curdir
    csm = [f for f in os.listdir(process_dir) if f[-3:].upper() == 'CSM']
    csm_fle = csm[0]
    old_maildate = ""
    pretty_maildate = ""

    if not os.path.isfile(os.path.join(process_dir, "{0}_.csm".format(csm_fle[:-4]))):
        shutil.copyfile(os.path.join(process_dir, csm_fle),
                        os.path.join(process_dir, "_{0}.csm_orig".format(csm_fle[:-4])))

    with open(os.path.join(process_dir, csm_fle), 'r') as f:
        old_maildate = (f.readline()[102:110])
        pretty_maildate = "{}-{}-{}".format(old_maildate[0:4],
                                            old_maildate[4:6],
                                            old_maildate[-2:])

    ans = input(f"Old mail date is {pretty_maildate}\nNew maildate? (YYYYMMDD): ")
    ans = ''.join(i for i in ans if i.isdigit())
    while len(ans) != 8:
        ans = input(f"Old mail date is {pretty_maildate}\nNew maildate? (YYYYMMDD): ")
        ans = ''.join(i for i in ans if i.isdigit())

    # ans = '20191022'

    with open(os.path.join(process_dir, "_{0}.csm_orig".format(csm_fle[:-4])), 'r') as source:
        with open(os.path.join(process_dir, csm_fle), 'w+', newline='') as target:
            for n, line in enumerate(source):
                part1 = line[0:102]
                part2 = line[110:137]
                part3 = line[145:176]
                part4 = line[184:]

                target.writelines(f"{part1}{ans}{part2}{ans}{part3}{ans}{part4}")

    print("Processing Complete")
    time.sleep(1.25)


def main():
    set_maildate()


if __name__ == '__main__':
    main()
