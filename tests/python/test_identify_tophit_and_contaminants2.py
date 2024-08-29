import os
import pytest
import sys
import json

# The scripts for this repo are in the script_dir.
# We want to import the functions we're testing from the script and add to PYTHONPATH.
# data_dir_name contains path to kraken reports needed for testing.
# We test against outputs generated by original Perl script.

this_file_dir = os.path.dirname(os.path.abspath(__file__))
data_dir_name = os.path.join('data', 'identify-tophit-and-contaminants2')
data_dir = os.path.join(this_file_dir, data_dir_name)
# path to script we are testing
script_dir = os.path.join(this_file_dir, os.pardir, os.pardir, 'bin')
sys.path.insert(1, script_dir)
sys.dont_write_bytecode = True
resources_dir = os.path.join(this_file_dir, os.pardir, os.pardir, 'resources')

import identify_tophit_and_contaminants2

def test_mykrobe_report_file():
    # test non existing mykrobe report
    args = [0, "nonexisting.json", os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', resources_dir, 'null', 'no']
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: cannot find %s' %args[1]

    # test empty mykrobe report
    args = [0, os.path.join(data_dir_name, "test_empty_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', resources_dir, 'null', 'no']
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: %s is empty' %args[1]

def test_kraken_report_file():
    # test non existing kraken report
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), "nonexisting.json", os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', resources_dir, 'null', 'no']
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: cannot find %s' %args[2]

    # test empty kraken report
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_empty_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', resources_dir, 'null', 'no']
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: %s is empty' %args[2]

def test_assembly_file():
    # test non existing assembly report
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"),'nonexisting.txt', 'null', 'no', resources_dir, 'null', 'no']
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: cannot find %s' %args[3]

    # test empty assembly
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_empty.txt"), 'null', 'no', resources_dir, 'null', 'no']
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: %s is empty' %args[3]
    
def test_non_existing_myco_dir():
    # test empty assembly
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', os.path.join(data_dir_name, "empty_dir"), 'null', 'no']
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: cannot find %s' %args[6]

def test_prev_species():
    # test non existing kraken report
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', resources_dir, 'nonexisting.json', "no"]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: cannot find %s' %args[7]

    # test empty kraken report
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', resources_dir, os.path.join(data_dir_name, "test_empty_report.json"), "no"]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: %s is empty' %args[7]

def test_supposed_species():
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'Randoms', 'no', resources_dir, 'null', "no"]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: if you provide a species ID, it must be one of either: abscessus|africanum|avium|bovis|chelonae|chimaera|fortuitum|intracellulare|kansasii|tuberculosis'

def test_unmix_myco():
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'test', resources_dir, 'null', "no"]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == 'ERROR: \'unmix myco\' should be either \'yes\' or \'no\''

def test_unmatched_ids():
    # mismatched mykrobe and kraken
    args = [0, os.path.join(data_dir_name, "mismatched_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', resources_dir, 'null', "no"]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == "ERROR: the sample IDs of %s and %s are mismatched" %(args[1], args[2])

    # test mismatched previous species id
    args = [0, os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), os.path.join(data_dir_name, "assembly_summary_refseq.txt"), 'null', 'no', resources_dir, os.path.join(data_dir_name, "mismatched_species_in_sample.json"), "no"]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        identify_tophit_and_contaminants2.process_requirements(args)

    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == "ERROR: sample ID of the previous species JSON (%s) does not match the sample ID we have from the Kraken and afanc reports (%s)" %(args[7], 'test')

def test_read_assembly_summary():
    # test reading assembly data
    assembly_file = "assembly_summary_refseq_short.txt"
    assembly_result_urls = "assembly_urls.json"
    assembly_result_tax_ids = "assembly_tax_ids.json"

    with open(os.path.join(data_dir_name, assembly_result_urls), 'r') as f:
        assembly_result_urls_json = json.load(f)
    with open(os.path.join(data_dir_name, assembly_result_tax_ids), 'r') as f:
        assembly_result_tax_ids_json = json.load(f)

    got_urls, got_tax_ids = identify_tophit_and_contaminants2.read_assembly_summary(os.path.join(data_dir_name, assembly_file))

    assert got_tax_ids == assembly_result_tax_ids_json

def test_process_data_unmix_myco_no():
    unmix_myco = 'no'
    assembly_file = "assembly_summary_refseq.txt"
    test_out = "test_species_in_sample_unmix_myco_no.json"
    test_out_urls = "test_urllist_unmix_myco_no.txt"

    urls, tax_ids = identify_tophit_and_contaminants2.read_assembly_summary(os.path.join(data_dir_name, assembly_file))
    # process reports
    out, out_urls = identify_tophit_and_contaminants2.process_reports(os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), 'null', unmix_myco, resources_dir, 'null', urls, tax_ids, 'test', 'yes')


    with open(os.path.join(data_dir_name, test_out), 'r') as f:
        test_out_json = json.load(f)
    test_out_urls_list = []
    with open(os.path.join(data_dir_name, test_out_urls), 'r') as f:
        for l in f:
            test_out_urls_list.append(l.strip())
    # correct paths as tests are being run from some other folder
    out['top_hit']["file_paths"]["ref_fa"] = "../../resources/tuberculosis.fasta"
    out['top_hit']["file_paths"]["clockwork_ref_dir"] = "../../resources/tuberculosis"

    assert out == test_out_json
    assert out_urls == test_out_urls_list

def test_process_data_unmix_myco_yes():
    unmix_myco = 'yes'
    assembly_file = "assembly_summary_refseq.txt"
    test_out = "test_species_in_sample_unmix_myco_yes.json"
    test_out_urls = "test_urllist_unmix_myco_yes.txt"

    urls, tax_ids = identify_tophit_and_contaminants2.read_assembly_summary(os.path.join(data_dir_name, assembly_file))
    # process reports
    out, out_urls = identify_tophit_and_contaminants2.process_reports(os.path.join(data_dir_name, "test_mykrobe_report.json"), os.path.join(data_dir_name, "test_kraken_report.json"), 'null', unmix_myco, resources_dir, 'null', urls, tax_ids, 'test', 'no')


    with open(os.path.join(data_dir_name, test_out), 'r') as f:
        test_out_json = json.load(f)
    test_out_urls_list = []
    with open(os.path.join(data_dir_name, test_out_urls), 'r') as f:
        for l in f:
            test_out_urls_list.append(l.strip())
    # correct paths as tests are being run from some other folder
    out['top_hit']["file_paths"]["ref_fa"] = "../../resources/tuberculosis.fasta"
    out['top_hit']["file_paths"]["clockwork_ref_dir"] = "../../resources/tuberculosis"

    assert out == test_out_json
    assert out_urls == test_out_urls_list
    


