<div align="center">

# Build Your Own AI

**Learn AI, LLMs and agents by building them from scratch.**

A curated, free and open-source list of step-by-step guides for recreating the AI systems you use every day: from a 100-line autograd engine to a GPT, a RAG pipeline and a coding agent.

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Links](https://github.com/Shashwat-19/build-your-own-ai/actions/workflows/links.yml/badge.svg)](https://github.com/Shashwat-19/build-your-own-ai/actions/workflows/links.yml)

</div>

> *"What I cannot create, I do not understand."* — Richard Feynman

Every resource here is **free to read or watch**. Each entry is tagged with the language you will write, or **Explainer** for conceptual write-ups worth reading alongside the code. `[video]` marks video walkthroughs.

## Where to start

Not sure where to begin? Follow the stack from the bottom up:

1. **Foundations** → build a [neural network](#build-your-own-neural-network) and an [autograd engine](#build-your-own-autograd-engine)
2. **Language models** → a [tokenizer](#build-your-own-tokenizer), a [transformer](#build-your-own-transformer), then a [GPT](#build-your-own-gpt)
3. **Training** → [fine-tune](#build-your-own-fine-tuning-pipeline) it, then [align](#build-your-own-rlhf--reasoning-model) it
4. **Systems** → [serve it fast](#build-your-own-inference-engine), give it [retrieval](#build-your-own-rag-system), then turn it into an [agent](#build-your-own-ai-agent)

## Contents

**Foundations**
* [Neural Network](#build-your-own-neural-network)
* [Autograd Engine](#build-your-own-autograd-engine)
* [Tensor Library & GPU Kernels](#build-your-own-tensor-library--gpu-kernels)
* [Recurrent Language Model](#build-your-own-recurrent-language-model)

**Language Models**
* [Tokenizer](#build-your-own-tokenizer)
* [Word Embeddings](#build-your-own-word-embeddings)
* [Transformer](#build-your-own-transformer)
* [GPT](#build-your-own-gpt)
* [Llama](#build-your-own-llama)
* [Mixture of Experts](#build-your-own-mixture-of-experts)

**Training & Alignment**
* [Distributed Training](#build-your-own-distributed-training)
* [Fine-tuning Pipeline](#build-your-own-fine-tuning-pipeline)
* [RLHF & Reasoning Model](#build-your-own-rlhf--reasoning-model)

**Inference**
* [Inference Engine](#build-your-own-inference-engine)

**Vision, Audio & Generative Models**
* [Object Detector](#build-your-own-object-detector)
* [Vision Transformer](#build-your-own-vision-transformer)
* [CLIP](#build-your-own-clip)
* [Vision-Language Model](#build-your-own-vision-language-model)
* [Diffusion Model](#build-your-own-diffusion-model)
* [GAN](#build-your-own-gan)
* [Speech Recognition](#build-your-own-speech-recognition)

**Reinforcement Learning**
* [RL Agent](#build-your-own-rl-agent)
* [AlphaZero](#build-your-own-alphazero)

**Retrieval**
* [Vector Database](#build-your-own-vector-database)
* [RAG System](#build-your-own-rag-system)

**Agents**
* [AI Agent](#build-your-own-ai-agent)
* [Coding Agent](#build-your-own-coding-agent)
* [Multi-Agent System](#build-your-own-multi-agent-system)
* [MCP Server](#build-your-own-mcp-server)
* [Browser Agent](#build-your-own-browser-agent)
* [Agent Memory](#build-your-own-agent-memory)

**Shipping It**
* [Evaluation Harness](#build-your-own-evaluation-harness)
* [Production ML System](#build-your-own-production-ml-system)

**[Full Courses](#full-courses)** · **[Contributing](#contributing)**

---

## Foundations

### Build your own Neural Network

* [**Python**: _The spelled-out intro to neural networks and backpropagation_](https://www.youtube.com/watch?v=VMj-3S1tku0) `[video]`
* [**Python**: _Machine Learning for Beginners: An Introduction to Neural Networks_](https://victorzhou.com/blog/intro-to-neural-networks/)
* [**Python**: _CNNs, Part 1: An Introduction to Convolutional Neural Networks_](https://victorzhou.com/blog/intro-to-cnns-part-1/)
* [**Python**: _Neural Networks and Deep Learning_ (free online book)](http://neuralnetworksanddeeplearning.com/)

### Build your own Autograd Engine

* [**Python**: _micrograd: a tiny scalar-valued autograd engine_](https://github.com/karpathy/micrograd)
* [**Python**: _MiniTorch: a DIY teaching library for machine learning engineers_](https://minitorch.github.io/)
* [**Python**: _Autodidax: JAX core from scratch_](https://docs.jax.dev/en/latest/autodidax.html)
* [**Python**: _tinygrad: a deep learning framework you can read end to end_](https://github.com/tinygrad/tinygrad)

### Build your own Tensor Library & GPU Kernels

* [**Python**: _Tensor Puzzles: implement NumPy functions with broadcasting only_](https://github.com/srush/Tensor-Puzzles)
* [**Python**: _GPU Puzzles: learn CUDA programming through puzzles_](https://github.com/srush/GPU-Puzzles)
* [**Python**: _Triton tutorials: vector add, fused softmax, matmul and Flash Attention_](https://triton-lang.org/main/getting-started/tutorials/index.html)
* [**CUDA**: _GPU MODE lecture series_](https://github.com/gpu-mode/lectures)

### Build your own Recurrent Language Model

* [**Python**: _The Unreasonable Effectiveness of Recurrent Neural Networks_](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [**Python**: _min-char-rnn: a character-level RNN in 112 lines of NumPy_](https://gist.github.com/karpathy/d4dee566867f8291f086)
* [**Python**: _makemore: bigram, MLP, RNN and transformer character models_](https://github.com/karpathy/makemore)
* [**Explainer**: _Understanding LSTM Networks_](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

## Language Models

### Build your own Tokenizer

* [**Python**: _Let's build the GPT Tokenizer_](https://www.youtube.com/watch?v=zduSFxRajkE) `[video]`
* [**Python**: _minbpe: minimal byte-pair encoding used in LLM tokenisation_](https://github.com/karpathy/minbpe)
* [**Python**: _Hugging Face LLM Course: building a tokenizer, block by block_](https://huggingface.co/learn/llm-course/chapter6/1)

### Build your own Word Embeddings

* [**Explainer**: _The Illustrated Word2vec_](https://jalammar.github.io/illustrated-word2vec/)
* [**Python**: _Sentence Transformers: training embedding models_](https://sbert.net/docs/sentence_transformer/training_overview.html)

### Build your own Transformer

* [**Explainer**: _The Illustrated Transformer_](https://jalammar.github.io/illustrated-transformer/)
* [**Python**: _The Annotated Transformer_](https://nlp.seas.harvard.edu/annotated-transformer/)
* [**Python**: _Transformers from scratch_](https://peterbloem.nl/blog/transformers)
* [**Python**: _GPT in 60 Lines of NumPy_](https://jaykmody.com/blog/gpt-from-scratch/)
* [**Python**: _Attention Is All You Need, implemented in PyTorch_](https://github.com/hkproj/pytorch-transformer)
* [**Explainer**: _The Illustrated BERT, ELMo, and co._](https://jalammar.github.io/illustrated-bert/)

### Build your own GPT

* [**Python**: _Let's build GPT: from scratch, in code, spelled out_](https://www.youtube.com/watch?v=kCc8FmEb1nY) `[video]`
* [**Python**: _Let's reproduce GPT-2 (124M)_](https://www.youtube.com/watch?v=l8pRSuU81PU) `[video]`
* [**Python**: _nanoGPT: the simplest, fastest repository for training medium-sized GPTs_](https://github.com/karpathy/nanoGPT)
* [**Python**: _Build a Large Language Model (From Scratch)_](https://github.com/rasbt/LLMs-from-scratch)
* [**Python**: _nanochat: the full ChatGPT pipeline (tokenizer → pretraining → SFT → RL → web UI)_](https://github.com/karpathy/nanochat)
* [**C/CUDA**: _llm.c: GPT-2 training in raw C and CUDA_](https://github.com/karpathy/llm.c)
* [**Explainer**: _The Illustrated GPT-2_](https://jalammar.github.io/illustrated-gpt2/)

### Build your own Llama

* [**Python**: _llama3 from scratch, one matrix multiplication at a time_](https://github.com/naklecha/llama3-from-scratch)
* [**Python**: _Coding LLaMA 2 from scratch in PyTorch_](https://github.com/hkproj/pytorch-llama)
* [**C**: _llama2.c: Llama 2 inference in one file of pure C_](https://github.com/karpathy/llama2.c)

### Build your own Mixture of Experts

* [**Explainer**: _Mixture of Experts Explained_](https://huggingface.co/blog/moe)
* [**Python**: _makeMoE: a sparse mixture-of-experts language model from scratch_](https://github.com/AviSoori1x/makeMoE)

## Training & Alignment

### Build your own Distributed Training

* [**Explainer**: _The Ultra-Scale Playbook: training LLMs on GPU clusters_](https://huggingface.co/spaces/nanotron/ultrascale-playbook)
* [**Python**: _picotron: minimal 4D parallelism (data, tensor, pipeline, context)_](https://github.com/huggingface/picotron)

### Build your own Fine-tuning Pipeline

* [**Python**: _Classification and instruction fine-tuning (Build a LLM From Scratch, ch. 6–7)_](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch07)
* [**Python**: _LoRA from scratch (Build a LLM From Scratch, appendix E)_](https://github.com/rasbt/LLMs-from-scratch/tree/main/appendix-E)
* [**Python**: _LoRA: the reference implementation from the paper authors_](https://github.com/microsoft/LoRA)
* [**Python**: _Unsloth notebooks: free Colab fine-tuning recipes_](https://github.com/unslothai/notebooks)

### Build your own RLHF & Reasoning Model

* [**Explainer**: _Illustrating Reinforcement Learning from Human Feedback_](https://huggingface.co/blog/rlhf)
* [**Explainer**: _The RLHF Book_](https://rlhfbook.com/)
* [**Python**: _Direct Preference Optimization from scratch_](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch07/04_preference-tuning-with-dpo)
* [**Python**: _Build a Reasoning Model (From Scratch)_](https://github.com/rasbt/reasoning-from-scratch)
* [**Python**: _TinyZero: reproduce DeepSeek R1-Zero's "aha moment" for under $30_](https://github.com/Jiayi-Pan/TinyZero)
* [**Python**: _simple_GRPO: a minimal GRPO implementation_](https://github.com/lsdefine/simple_GRPO)
* [**Python**: _Open R1: a fully open reproduction of DeepSeek-R1_](https://github.com/huggingface/open-r1)

## Inference

### Build your own Inference Engine

* [**Python**: _Understanding and coding the KV cache from scratch_](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)
* [**Explainer**: _A Visual Guide to Quantization_](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization)
* [**Python**: _gpt-fast: fast transformer inference in under 1,000 lines of PyTorch_](https://github.com/pytorch-labs/gpt-fast)
* [**Python**: _nano-vllm: a lightweight vLLM built from scratch_](https://github.com/GeeeekExplorer/nano-vllm)
* [**C++**: _llama.cpp: LLM inference in C/C++_](https://github.com/ggml-org/llama.cpp)

## Vision, Audio & Generative Models

### Build your own Object Detector

* [**Python**: _YOLOv3 from scratch in PyTorch_](https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLOv3)
* [**Python**: _TorchVision object detection fine-tuning tutorial_](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)

### Build your own Vision Transformer

* [**Python**: _vit-pytorch: Vision Transformer and its variants in PyTorch_](https://github.com/lucidrains/vit-pytorch)

### Build your own CLIP

* [**Python**: _A simple PyTorch implementation of OpenAI CLIP_](https://github.com/moein-shariatnia/OpenAI-CLIP)

### Build your own Vision-Language Model

* [**Python**: _nanoVLM: the simplest repository to train a small VLM_](https://github.com/huggingface/nanoVLM)
* [**Python**: _seemore: a vision-language model from scratch_](https://github.com/AviSoori1x/seemore)

### Build your own Diffusion Model

* [**Explainer**: _What are Diffusion Models?_](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
* [**Python**: _The Annotated Diffusion Model_](https://huggingface.co/blog/annotated-diffusion)
* [**Python**: _minDiffusion: self-contained, minimal DDPM_](https://github.com/cloneofsimo/minDiffusion)
* [**Python**: _Stable Diffusion from scratch in PyTorch_](https://github.com/hkproj/pytorch-stable-diffusion)
* [**Python**: _fast.ai Part 2: From Deep Learning Foundations to Stable Diffusion_](https://course.fast.ai/Lessons/part2.html)

### Build your own GAN

* [**Python**: _DCGAN tutorial: generate faces with PyTorch_](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)

### Build your own Speech Recognition

* [**Python**: _Whisper: OpenAI's reference implementation_](https://github.com/openai/whisper)
* [**C++**: _whisper.cpp: Whisper inference in plain C/C++_](https://github.com/ggml-org/whisper.cpp)
* [**Python**: _Hugging Face Audio Course_](https://huggingface.co/learn/audio-course)

## Reinforcement Learning

### Build your own RL Agent

* [**Python**: _Spinning Up in Deep RL_](https://spinningup.openai.com/)
* [**Python**: _Hugging Face Deep RL Course_](https://huggingface.co/learn/deep-rl-course)
* [**Python**: _Reinforcement Learning (DQN) tutorial_](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)
* [**Python**: _CleanRL: single-file implementations of PPO, DQN, SAC and more_](https://github.com/vwxyzjn/cleanrl)

### Build your own AlphaZero

* [**Python**: _A Simple Alpha(Go) Zero Tutorial_](https://suragnair.github.io/posts/alphazero.html)
* [**Python**: _alpha-zero-general: AlphaZero for any game_](https://github.com/suragnair/alpha-zero-general)

## Retrieval

### Build your own Vector Database

* [**Explainer**: _Hierarchical Navigable Small Worlds (HNSW)_](https://www.pinecone.io/learn/series/faiss/hnsw/)
* [**C++**: _hnswlib: header-only HNSW you can read in an afternoon_](https://github.com/nmslib/hnswlib)

### Build your own RAG System

* [**Python**: _RAG From Scratch_](https://github.com/langchain-ai/rag-from-scratch)
* [**Explainer**: _Introducing Contextual Retrieval_](https://www.anthropic.com/news/contextual-retrieval)
* [**Python**: _RAG Techniques: 30+ advanced retrieval techniques as notebooks_](https://github.com/NirDiamant/RAG_Techniques)
* [**Python**: _nano-graphrag: a simple, hackable GraphRAG_](https://github.com/gusye1234/nano-graphrag)
* [**Python**: _GraphRAG: Microsoft's graph-based RAG_](https://github.com/microsoft/graphrag)

## Agents

### Build your own AI Agent

* [**Explainer**: _Building Effective Agents_](https://www.anthropic.com/engineering/building-effective-agents)
* [**Explainer**: _LLM Powered Autonomous Agents_](https://lilianweng.github.io/posts/2023-06-23-agent/)
* [**Python**: _A simple Python implementation of the ReAct pattern_](https://til.simonwillison.net/llms/python-react-pattern)
* [**Python**: _Hugging Face Agents Course_](https://huggingface.co/learn/agents-course)
* [**Python**: _smolagents: agents that think in code_](https://github.com/huggingface/smolagents)
* [**Python**: _AI Agents for Beginners (Microsoft)_](https://github.com/microsoft/ai-agents-for-beginners)
* [**Python**: _GenAI Agents: tutorials from simple to advanced_](https://github.com/NirDiamant/GenAI_Agents)

### Build your own Coding Agent

* [**Go**: _How to Build an Agent_](https://ampcode.com/how-to-build-an-agent)
* [**Python**: _mini-swe-agent: a 100-line agent that solves GitHub issues_](https://github.com/SWE-agent/mini-swe-agent)
* [**Python**: _SWE-agent: the full research system_](https://github.com/SWE-agent/SWE-agent)

### Build your own Multi-Agent System

* [**Explainer**: _How we built our multi-agent research system_](https://www.anthropic.com/engineering/multi-agent-research-system)
* [**Python**: _Swarm: educational framework for agent handoffs_](https://github.com/openai/swarm)
* [**Python**: _OpenAI Agents SDK_](https://github.com/openai/openai-agents-python)
* [**Python**: _AutoGen_](https://github.com/microsoft/autogen)

### Build your own MCP Server

* [**Python/TypeScript**: _Build an MCP server (official quickstart)_](https://modelcontextprotocol.io/quickstart/server)
* [**Python**: _MCP Python SDK_](https://github.com/modelcontextprotocol/python-sdk)
* [**TypeScript**: _MCP TypeScript SDK_](https://github.com/modelcontextprotocol/typescript-sdk)
* [**Python/TypeScript**: _Reference MCP servers_](https://github.com/modelcontextprotocol/servers)

### Build your own Browser Agent

* [**Python**: _browser-use: make websites accessible to AI agents_](https://github.com/browser-use/browser-use)

### Build your own Agent Memory

* [**Python**: _Letta (MemGPT): stateful agents with self-editing memory_](https://github.com/letta-ai/letta)
* [**Python**: _mem0: a memory layer for AI agents_](https://github.com/mem0ai/mem0)

## Shipping It

### Build your own Evaluation Harness

* [**Explainer**: _Your AI Product Needs Evals_](https://hamel.dev/blog/posts/evals/)
* [**Python**: _Inspect: the UK AI Security Institute's eval framework_](https://github.com/UKGovernmentBEIS/inspect_ai)
* [**Python**: _lm-evaluation-harness_](https://github.com/EleutherAI/lm-evaluation-harness)
* [**Python**: _OpenAI Evals_](https://github.com/openai/evals)
* [**TypeScript**: _promptfoo: test and red-team LLM apps_](https://github.com/promptfoo/promptfoo)

### Build your own Production ML System

* [**Python**: _Made With ML: design, develop, deploy and iterate on ML systems_](https://github.com/GokuMohandas/Made-With-ML)
* [**Python**: _MLOps Zoomcamp_](https://github.com/DataTalksClub/mlops-zoomcamp)
* [**Python**: _LLM Zoomcamp_](https://github.com/DataTalksClub/llm-zoomcamp)

---

## Full Courses

Free, end-to-end curricula for when you want structure rather than a single project.

* [**Neural Networks: Zero to Hero**](https://karpathy.ai/zero-to-hero.html): Andrej Karpathy, backprop to GPT `[video]`
* [**Stanford CS336: Language Modeling from Scratch**](https://cs336.stanford.edu/)
* [**Stanford CS231n: Deep Learning for Computer Vision**](https://cs231n.github.io/)
* [**Stanford CS224n: NLP with Deep Learning**](https://web.stanford.edu/class/cs224n/)
* [**MIT 6.S191: Introduction to Deep Learning**](http://introtodeeplearning.com/) `[video]`
* [**fast.ai: Practical Deep Learning for Coders**](https://course.fast.ai/) `[video]`
* [**Dive into Deep Learning**](https://d2l.ai/): interactive book with code in PyTorch, JAX and TensorFlow
* [**Hugging Face LLM Course**](https://huggingface.co/learn/llm-course)
* [**Anthropic Courses**](https://github.com/anthropics/courses): prompt engineering, tool use, real-world prompting
* [**Claude Cookbooks**](https://github.com/anthropics/claude-cookbooks): runnable recipes for RAG, tool use and agents

---

## Contributing

Found a great tutorial? Spotted a dead link? Contributions are very welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first; the bar is simple: **it must be free, and it must teach you to build the thing, not just use it.**

## Acknowledgements

Inspired by [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x). All credit for the tutorials goes to their authors.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this list. The linked resources keep their own licences.
