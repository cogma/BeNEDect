import csv
import glob
import json

mctest_path = "raw_data/mctest"
race_path = "raw_data/race"
reclor_path = "raw_data/reclor_data"


def read_mctest_data():
    if glob.glob(f"{mctest_path}/mc500.train.tsv") == []:
        print(f"put `mc{160,500}.train.tsv` in {mctest_path}")
        exit(1)
    if glob.glob(f"{mctest_path}/mc160.train.tsv") == []:
        print(f"put `mc{160,500}.train.tsv` in {mctest_path}")
        exit(1)
    items = {}
    with open(f"{mctest_path}/mc160.train.tsv") as f:
        for row in csv.reader(f, delimiter="\t"):
            items[row[0]] = row[2]
    with open(f"{mctest_path}/mc500.train.tsv") as f:
        for row in csv.reader(f, delimiter="\t"):
            items[row[0]] = row[2]
    return items


def read_race_data():
    if glob.glob(f"{race_path}/train/*") == []:
        print(f"put `train` directory in {race_path}")
        exit(1)
    items = {}
    for filepath in glob.glob(f"{race_path}/train/*/*.txt"):
        with open(filepath) as f:
            data = json.load(f)
            pas_id = "/".join(filepath.split("/")[2:])
            items[f"race/{pas_id}"] = data["article"]
    return items


def read_reclor_data():
    if glob.glob(f"{reclor_path}/train.json") == []:
        print(f"put `train.json` in {reclor_path}")
        exit(1)
    reclor_data = json.load(open(f"{reclor_path}/train.json"))
    return {f"reclor_{v['id_string']}": v["context"] for v in reclor_data}


def main():
    input_file = "BeNEDect_partial.json"
    output_file = "BeNEDect_all.json"

    partial_data = json.load(open(input_file))
    raw_data = {}
    raw_data.update(read_mctest_data())
    raw_data.update(read_race_data())
    raw_data.update(read_reclor_data())

    for data in partial_data.values():
        if data["passage_id"].startswith("mc"):
            data["correct_passage"] = raw_data[data["passage_id"]]
            data["error_passage"] = (
                data["correct_passage"][: data["target_start_char"]]
                + data["error_number"]
                + data["correct_passage"][data["target_end_char"] :]
            )
        elif data["passage_id"].startswith("race"):
            data["correct_passage"] = raw_data[data["passage_id"]]
            data["error_passage"] = (
                data["correct_passage"][: data["target_start_char"]]
                + data["error_number"]
                + data["correct_passage"][data["target_end_char"] :]
            )
        elif data["passage_id"].startswith("reclor"):
            data["correct_passage"] = raw_data[data["passage_id"]]
            data["error_passage"] = (
                data["correct_passage"][: data["target_start_char"]]
                + data["error_number"]
                + data["correct_passage"][data["target_end_char"] :]
            )

    with open(output_file, "w") as f:
        json.dump(partial_data, f, indent=4)


if __name__ == "__main__":
    main()
